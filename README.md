# 🛒 E-Commerce Product Search Agent

A powerful AI-driven product search application that searches across multiple e-commerce platforms using MCP (Model Context Protocol) tools and LangChain.

## 🚀 Features

- **Multi-Platform Search**: Search across 7 major e-commerce platforms
- **AI-Powered**: Uses OpenAI GPT-4 and LangChain for intelligent search
- **Real-time Results**: Instant product recommendations with ratings and URLs
- **Modern UI**: Clean Streamlit interface with chat-like input
- **Platform Selection**: Easy checkbox selection for target platforms
- **Professional Results**: Organized results by platform with product details

## 🛍️ Supported Platforms

- **Amazon** - World's largest online retailer
- **Best Buy** - Electronics and appliances
- **Ebay** - Online marketplace and auctions
- **Walmart** - Retail giant with online presence
- **Target** - Department store chain
- **Costco** - Membership-based warehouse club
- **Newegg** - Computer hardware and electronics

## 🛠️ Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Environment Variables

Create a `.env` file in your project directory:

```env
# Brightdata API credentials
API_TOKEN=your_brightdata_api_token
BROWSER_AUTH=your_browser_auth_token
WEB_UNLOCKER_ZONE=your_web_unlocker_zone

# OpenAI API key (for LangChain)
OPENAI_API_KEY=your_openai_api_key
```

### 3. Get API Keys

#### Brightdata API
1. Visit [Brightdata](https://brightdata.com/)
2. Create an account
3. Get your API token, browser auth, and web unlocker zone
4. Add them to your `.env` file

#### OpenAI API
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Create an account or sign in
3. Go to API Keys section
4. Create a new API key
5. Add it to your `.env` file

### 4. Run the Application

```bash
streamlit run ecom.py
```

## 🎯 How It Works

### 1. **Platform Selection**
- Users select target platforms using checkboxes in the sidebar
- Default selection includes Amazon and Best Buy
- Multiple platforms can be selected simultaneously

### 2. **Search Query**
- Users enter search queries in a chat-like interface
- Examples: "wireless headphones", "gaming laptop", "coffee maker"
- Press Enter to initiate search

### 3. **AI-Powered Search**
- LangChain orchestrates the search process
- MCP tools handle platform-specific data extraction
- GPT-4 provides intelligent search optimization

### 4. **Results Display**
- Results organized by platform
- Product titles, ratings, and URLs displayed
- Summary shows total products found across platforms

## 🏗️ Architecture

```
User Input → Platform Selection → AI Agent → MCP Tools → Platform Scraping → Results Display
```

### **Technical Stack**
- **Frontend**: Streamlit
- **AI Framework**: LangChain
- **LLM**: OpenAI GPT-4
- **Data Extraction**: MCP (Model Context Protocol)
- **Platform Access**: Brightdata API

## 📊 Features Breakdown

### **Search Interface**
- **Chat Input**: Modern chat-like search interface
- **Platform Checkboxes**: Easy multi-platform selection
- **Real-time Feedback**: Loading indicators and progress updates

### **Results Display**
- **Platform Organization**: Results grouped by platform
- **Product Details**: Title, rating, and direct URL
- **Summary Statistics**: Total products and platforms searched

### **Error Handling**
- **API Validation**: Checks for required API keys
- **Graceful Failures**: Handles platform-specific errors
- **User Feedback**: Clear error messages and suggestions

## 🔧 Configuration

### **Environment Variables**
- `API_TOKEN`: Brightdata API authentication
- `BROWSER_AUTH`: Browser authentication token
- `WEB_UNLOCKER_ZONE`: Web unlocker configuration
- `OPENAI_API_KEY`: OpenAI API for LangChain

### **Default Settings**
- **Default Platforms**: Amazon, Best Buy
- **Model**: GPT-4 (gpt-4o)
- **Layout**: Wide layout for better results display

## 🚀 Usage Examples

### **Basic Search**
```
Query: "wireless headphones"
Platforms: Amazon, Best Buy
Result: Headphones from both platforms with ratings and URLs
```

### **Multi-Platform Search**
```
Query: "gaming laptop"
Platforms: Amazon, Best Buy, Newegg
Result: Gaming laptops from all three platforms
```

### **Specific Product Search**
```
Query: "iPhone 15 Pro"
Platforms: Amazon, Walmart, Target
Result: iPhone 15 Pro listings with prices and availability
```

## 🛠️ Customization

### **Adding New Platforms**
1. Add platform name to `PLATFORMS` list
2. Update MCP tools configuration
3. Test platform-specific data extraction

### **Modifying Search Behavior**
- Edit `SYSTEM_PROMPT` for different search strategies
- Adjust LangChain agent parameters
- Customize result display format

### **UI Customization**
- Modify Streamlit layout and styling
- Add custom CSS for branding
- Implement additional result filters

## 🐛 Troubleshooting

### **API Key Issues**
- Ensure all required API keys are set in `.env`
- Verify API key permissions and quotas
- Check network connectivity

### **Platform Access Issues**
- Verify Brightdata account status
- Check platform-specific access permissions
- Ensure proper browser authentication

### **Search Failures**
- Try simpler search queries
- Select fewer platforms for testing
- Check OpenAI API quota and billing

## 📈 Performance

- **Fast Search**: Optimized for sub-30 second response times
- **Scalable**: Can handle multiple platforms simultaneously
- **Reliable**: Robust error handling and retry mechanisms
- **Efficient**: Minimal API calls through intelligent caching

## 🔒 Security

- **API Key Protection**: Environment variables for sensitive data
- **Secure Communication**: HTTPS for all API calls
- **No Data Storage**: Results not persisted locally
- **Privacy Focused**: No user data collection

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 🆘 Support

For issues and questions:
- Check the troubleshooting section
- Review API documentation
- Open an issue on GitHub

---

**Built with ❤️ using Streamlit, LangChain, and MCP** 
