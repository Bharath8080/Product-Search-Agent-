import os
import json
import asyncio
from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseModel, Field
import streamlit as st
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters

from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent


load_dotenv()
model = ChatOpenAI(model='gpt-4o')

# Filter out None values from environment variables
env_vars = {}
for key, value in {
    'API_TOKEN': os.getenv('API_TOKEN'),
    'BROWSER_AUTH': os.getenv('BROWSER_AUTH'),
    'WEB_UNLOCKER_ZONE': os.getenv('WEB_UNLOCKER_ZONE')
}.items():
    if value is not None:
        env_vars[key] = value

server_params = StdioServerParameters(
    command='npx',
    args=['@brightdata/mcp'],
    env=env_vars
)

SYSTEM_PROMPT = (
    "To find products, first use the search_engine tool. When finding products, use the web_data tool for the platform. If none exists, scrape as markdown."
    "Example: Don't use web_data_bestbuy_products for search. Use it only for getting data on specific products you already found in search."
)

PLATFORMS = ['Amazon', 'Best Buy', 'Ebay', 'Walmart', 'Target', 'Costco', 'Newegg']




class Hit(BaseModel):
    url: str = Field(..., description='The URL of the product that was found')
    title: str = Field(..., description='The title of the product that was found')
    rating: str = Field(..., description='The rating of the product (stars, number of ratings given etc.)')


class PlatformBlock(BaseModel):
    platform: str = Field(..., description='Name of the platform')
    results: list[Hit] = Field(..., description='List of results for this platform')


class ProductSearchResponse(BaseModel):
    platforms: list[PlatformBlock] = Field(..., description='Aggregated list of all results grouped by platform')


async def run_agent(query, platforms):
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as sess:
            await sess.initialize()

            tools = await load_mcp_tools(sess)

            agent = create_react_agent(model, tools, response_format=ProductSearchResponse)

            prompt = f'{query}\n\nPlatforms: {",".join(platforms)}'

            result = await agent.ainvoke(
                {
                    'messages': [
                        {'role': 'system', 'content': SYSTEM_PROMPT},
                        {'role': 'user', 'content': prompt}
                    ]
                }
            )

            structured = result['structured_response']

            return structured.model_dump()


def main():
    st.set_page_config(
        page_title="Product Search Agent",
        page_icon="🛒",
        layout="wide"
    )
    # Sidebar logo
    st.sidebar.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTP00Eo8E_ReEmKbKKkjcYDrPjCDZf1CJtRA&s", use_container_width=True)
    st.markdown(
    """
    <h2 style="display: flex; align-items: center;">
        <img src="https://registry.npmmirror.com/@lobehub/icons-static-png/1.51.0/files/light/mcp.png" width="50" style="margin-right: 7px;"> 
         Product Search Agent 🛒
        
        
    </h2>
    """,
    unsafe_allow_html=True
)
    st.markdown("Search for products across multiple platforms using AI-powered MCP tools.")

    # Sidebar for platform selection
    st.sidebar.header("📱 Select Platforms")
    st.sidebar.write("Choose platforms to search:")
    
    # Create checkboxes for each platform
    selected_platforms = []
    for platform in PLATFORMS:
        if st.sidebar.checkbox(platform, value=(platform in ['Amazon', 'Best Buy'])):
            selected_platforms.append(platform)
    
    # Search query input
    query = st.chat_input(
        "Enter your search query (e.g., wireless headphones, gaming laptop...)"
    )
    

    
    # Handle search query
    if query:
        if not query.strip():
            st.error("Please enter a search query.")
        elif not selected_platforms:
            st.error("Please select at least one platform.")
        else:
            with st.spinner("Searching for products across platforms..."):
                try:
                    response_json = asyncio.run(run_agent(query, selected_platforms))
                    display_results(response_json, query)
                except Exception as exc:
                    st.error(f"Agent error: {exc}")
                    st.exception(exc)
    



def display_results(response_json, query):
    """Display search results in a nice format"""
    if not response_json or 'platforms' not in response_json:
        st.warning("No results found. Try a different search query.")
        return
    
    st.header(f"📦 Search Results for: '{query}'")
    
    # Store results in session state
    st.session_state.previous_results = response_json
    st.session_state.previous_query = query
    
    # Display results by platform
    for platform_block in response_json['platforms']:
        platform_name = platform_block['platform']
        results = platform_block['results']
        
        # Create platform header
        st.subheader(f"🛒 {platform_name} ({len(results)} results)")
        
        # Display results
        if not results:
            st.info(f"No results found on {platform_name}")
        else:
            for i, hit in enumerate(results, 1):
                with st.container():
                    col1, col2 = st.columns([1, 4])
                    
                    with col1:
                        st.markdown(f"**{i}.**")
                    
                    with col2:
                        st.markdown(f"**{hit['title']}**")
                        st.caption(f"Rating: {hit['rating']}")
                        st.caption(f"URL: {hit['url']}")
                    
                    if i < len(results):
                        st.divider()
    
    # Summary
    total_results = sum(len(platform['results']) for platform in response_json['platforms'])
    st.success(f"Found {total_results} products across {len(response_json['platforms'])} platforms!")


if __name__ == "__main__":
    main()
