# BMW Sales Data Analysis with LLM

A comprehensive LLM-powered system for analyzing BMW sales data (2020-2024), generating visualizations, and producing automated business intelligence reports.

## 🎯 Features

- **Automated Data Cleaning**: Removes duplicates, handles missing values, detects outliers
- **Statistical Analysis**: Comprehensive analysis of sales trends, regional performance, model performance
- **Data Visualization**: Professional charts and graphs using matplotlib and seaborn
- **LLM-Powered Insights**: Supports both OpenAI (GPT-4/GPT-3.5-turbo) and Google Gemini (Pro/Flash) to generate executive summaries, strategic recommendations, and creative business insights
- **Multi-Provider Support**: Flexible LLM provider configuration - choose based on quality, speed, and cost needs
- **Role-Based Analysis**: Toggle between detailed analyst-level and executive-level strategic insights
- **Automated Reporting**: Generates professional HTML and Markdown reports
- **Reproducible**: Consistent report structure with minor variations due to LLM stochasticity

## 📋 Requirements

- Python 3.12
- LLM API Key (OpenAI or Google Gemini)
- BMW sales data file: `data-bmw/BMW sales data (2020-2024).xlsx`

## 🚀 Quick Start

### 1. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 2. Configure API Key

Create a `.env` file in the project root:

```powershell
Copy-Item .env.example .env
```

Edit `.env` and add your LLM API key:

```
# Choose your LLM provider
LLM_PROVIDER=openai  # or 'gemini'

# If using OpenAI:
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4

# If using Google Gemini:
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-1.5-flash

LLM_TEMPERATURE=0.7
ROLE=Business Analyst
```

**Configuration Options:**

**LLM Provider:**
- `openai` - Use OpenAI GPT models (GPT-4 or GPT-3.5-turbo)
- `gemini` - Use Google Gemini models (Gemini 1.5 Pro or Flash)

**OpenAI Models** (when `LLM_PROVIDER=openai`):
- `gpt-4`: Higher quality, ~$0.30-$0.60/report
- `gpt-3.5-turbo`: Faster, cheaper, ~$0.03-$0.06/report

**Gemini Models** (when `LLM_PROVIDER=gemini`):
- `gemini-1.5-pro`: Best quality, balanced performance
- `gemini-1.5-flash`: Fastest, most cost-effective, ~$0.01-$0.02/report

**Other Options:**
- **LLM_TEMPERATURE**: 0.0 (deterministic) to 1.0 (creative), recommended: 0.7
- **ROLE**: Choose analysis depth
  - `Business Analyst` (default): Detailed, comprehensive 4-5 paragraph analyses per section
  - `Business Chief`: Executive-level strategic insights with BLUF structure, BCG Matrix, Pareto analysis

### 3. Prepare Data

Place your BMW sales data file in the `data-bmw` folder:
- File name: `BMW sales data (2020-2024).xlsx`
- Required columns: Model, Year, Region, Color, Fuel_Type, Transmission, Engine_Size_L, Mileage_KM, Price_USD, Sales_Volume

### 4. Clean the Data

```powershell
python read_bmw_data.py
```

This will:
- Load and validate the raw data
- Remove duplicates and blank rows
- Handle missing values
- Remove outliers
- Create derived features
- Save cleaned data as: `data-bmw/BMW sales data (2020-2024) Cleaned.xlsx`

### 5. Run the Analysis

```powershell
python analyze_bmw_sales.py
```

This will:
1. Perform statistical analysis on cleaned data
2. Generate 8 professional visualizations
3. Use OpenAI GPT-4 to generate insights
4. Create comprehensive HTML and Markdown reports

## 📊 Output

The system generates the following outputs in the `reports/` directory:

### Reports
- **BMW_Sales_Analysis_Report.html** - Interactive HTML report with embedded visualizations
- **BMW_Sales_Analysis_Report.md** - Markdown version for documentation

### Visualizations
1. `01_yearly_sales_trend.png` - Sales volume and average price over time
2. `02_regional_performance.png` - Sales by region and market share
3. `03_model_performance.png` - Model comparison with top performers highlighted
4. `04_price_analysis.png` - Price distribution and price-sales relationship
5. `05_fuel_type_trends.png` - Fuel type preferences over time
6. `06_revenue_analysis.png` - Revenue breakdown (if revenue data available)
7. `07_correlation_heatmap.png` - Correlation matrix of key metrics
8. `08_model_category_performance.png` - Performance by model category

## 📈 Analysis Sections

The generated report includes:

1. **Executive Summary** - High-level overview of key findings
2. **Key Performance Metrics** - Critical business metrics dashboard
3. **Yearly Sales Trends** - Performance trends from 2020-2024
4. **Regional Performance Analysis** - Top and underperforming markets
5. **Model Performance Analysis** - Product portfolio insights
6. **Price Drivers and Market Dynamics** - Price elasticity and sales drivers
7. **Creative Business Insights** - Unexpected patterns and opportunities
8. **Strategic Recommendations** - Actionable business recommendations

## 🏗️ Project Structure

```
data-science-bmw-llm/
├── data-bmw/
│   ├── BMW sales data (2020-2024).xlsx          # Raw data (you provide)
│   └── BMW sales data (2020-2024) Cleaned.xlsx  # Cleaned data (generated)
├── reports/                                       # Generated reports and charts
├── read_bmw_data.py                              # Data cleaning script
├── analyze_bmw_sales.py                          # Main analysis orchestrator
├── data_analyzer.py                              # Statistical analysis module
├── visualizer.py                                 # Visualization generation module
├── llm_insights.py                               # OpenAI LLM integration module
├── report_generator.py                           # Report generation module
├── requirements.txt                              # Python dependencies
├── .env.example                                  # Environment variable template
├── .env                                          # Your API keys (not tracked)
└── README.md                                     # This file
```

## 🔧 Module Details

### read_bmw_data.py
Loads raw data and performs comprehensive cleaning:
- Removes blank rows and duplicates
- Handles missing values (drop or fill based on column type)
- Removes outliers using IQR method (3×IQR)
- Validates data ranges (years 2020-2024, positive prices/sales, engine size 1.5-5.0L)
- Creates derived features (Total_Revenue, Price_Category, Model_Category, Mileage_Category)
- Standardizes text data (strip whitespace, consistent casing)

### data_analyzer.py
Performs statistical analysis:
- Overview metrics (total sales, average price, etc.)
- Yearly trends and year-over-year growth
- Regional performance and market share
- Model performance and portfolio analysis
- Price segment analysis and elasticity
- Fuel type and transmission trends
- Revenue analysis (if available)
- Correlation analysis

### visualizer.py
Generates professional visualizations:
- Line charts for trends over time
- Bar charts for comparisons
- Pie charts for market share
- Scatter plots for relationships
- Heatmaps for correlations
- Customized color schemes and annotations

### llm_insights.py
Integrates with OpenAI API to generate:
- Executive summary (3-4 paragraphs)
- Detailed analysis of yearly trends (4-5 paragraphs)
- Regional performance insights (4-5 paragraphs)
- Model performance analysis (4-5 paragraphs)
- Price drivers and key factors (4-5 paragraphs)
- Creative business insights (2 unique insights)
- Strategic recommendations (5-7 actionable items)

### report_generator.py
Creates comprehensive reports:
- Professional HTML report with embedded CSS
- Markdown report for documentation
- Combines statistical data, visualizations, and LLM insights
- Structured sections with table of contents
- Responsive design for HTML

## 🎨 LLM Configuration

The system supports multiple LLM providers with flexible configuration:

### Supported Providers
- **OpenAI**: GPT-4, GPT-3.5-turbo
- **Google Gemini**: Gemini 1.5 Pro, Gemini 1.5 Flash

### Analysis Modes
- **Business Analyst**: Detailed 4-5 paragraph analyses
- **Business Chief**: Executive BLUF-style strategic insights

**For detailed provider comparison, costs, and switching instructions, see [LLM_PROVIDER_GUIDE.md](LLM_PROVIDER_GUIDE.md)**

### LLM Guidance
The LLM is specifically guided to:

1. **Identify sales performance trends** - Analyze patterns over time and across regions
2. **Highlight top/underperforming models and markets** - Compare performance metrics
3. **Explore key sales drivers** - Price, market segment, model type, fuel type
4. **Generate creative insights** - Unexpected patterns, cross-market opportunities
5. **Provide business understanding** - Strategic recommendations with business impact

## 🔒 Security

- Never commit your `.env` file with API keys
- `.gitignore` is configured to exclude sensitive files
- API keys are loaded from environment variables only

## 📝 Notes

- The LLM temperature is set to 0.7 for balanced creativity and consistency
- Reports are reproducible with minor variations due to LLM stochasticity
- Report structure and coverage remain consistent across runs
- Visualizations are deterministic and always identical

## 🆘 Troubleshooting

### Error: "API key not found"
- Ensure `.env` file exists in project root
- Check the correct API key variable is set:
  - OpenAI: `OPENAI_API_KEY=your_key_here`
  - Gemini: `GEMINI_API_KEY=your_key_here`
- Verify `LLM_PROVIDER` matches your configured provider

### Error: "Unsupported LLM_PROVIDER"
- Set `LLM_PROVIDER=openai` or `LLM_PROVIDER=gemini` (lowercase)

### Error: "File not found"
- Ensure data file is named exactly: `BMW sales data (2020-2024).xlsx`
- Check file is in `data-bmw/` directory
- Run `read_bmw_data.py` before `analyze_bmw_sales.py`

### Error: "Module not found"
- Run: `pip install -r requirements.txt`
- For specific providers:
  - OpenAI: `pip install openai>=1.0.0`
  - Gemini: `pip install google-generativeai>=0.3.0`
- Ensure you're using Python 3.12

### LLM API Errors
- Verify your API key is valid and active
- Check you have available credits/quota
- Ensure internet connection is working
- OpenAI rate limits: Consider using GPT-3.5-turbo or wait
- Gemini rate limits: Check quota in Google Cloud Console

**For more provider-specific troubleshooting, see [LLM_PROVIDER_GUIDE.md](LLM_PROVIDER_GUIDE.md)**

## 💡 Alternative: Using Google Gemini (Free)

If you prefer to use Google's Gemini API (free quota available):

1. Get a free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Modify `llm_insights.py` to use Google's Gemini API instead of OpenAI
3. Update `.env` with `GEMINI_API_KEY=your_key_here`

## 📞 Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify all requirements are installed
3. Ensure data format matches expected structure

## 📄 License

This project is for educational and development purposes.

---

**Built with Python, OpenAI GPT-4, and Data Science Best Practices**
