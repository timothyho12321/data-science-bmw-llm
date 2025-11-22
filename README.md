# BMW Sales Data Analysis with LLM

A comprehensive LLM-powered system for analyzing BMW sales data (2020-2024), generating visualizations, and producing automated business intelligence reports.

## 🎯 Features

- **Automated Data Cleaning**: Removes duplicates, handles missing values, detects outliers
- **Statistical Analysis**: Comprehensive analysis of sales trends, regional performance, model performance
- **Data Visualization**: Professional charts and graphs using matplotlib and seaborn
- **LLM-Powered Insights**: Uses OpenAI GPT-4 to generate executive summaries, strategic recommendations, and creative business insights
- **Automated Reporting**: Generates professional HTML and Markdown reports
- **Reproducible**: Consistent report structure with minor variations due to LLM stochasticity

## 📋 Requirements

- Python 3.12
- OpenAI API Key
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

Edit `.env` and add your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4
OPENAI_TEMPERATURE=0.7
```

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

## 🎨 LLM Guidance

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

### Error: "OPENAI_API_KEY not found"
- Ensure `.env` file exists in project root
- Check that `OPENAI_API_KEY=your_key_here` is set correctly

### Error: "File not found"
- Ensure data file is named exactly: `BMW sales data (2020-2024).xlsx`
- Check file is in `data-bmw/` directory
- Run `read_bmw_data.py` before `analyze_bmw_sales.py`

### Error: "Module not found"
- Run: `pip install -r requirements.txt`
- Ensure you're using Python 3.12

### OpenAI API Errors
- Verify your API key is valid
- Check you have available credits
- Ensure internet connection is working
- Consider using GPT-3.5-turbo if rate limited: Set `OPENAI_MODEL=gpt-3.5-turbo` in `.env`

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
