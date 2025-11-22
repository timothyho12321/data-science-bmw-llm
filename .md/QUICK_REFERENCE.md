# Quick Reference Card

## 🚀 Quick Commands

### First Time Setup
```powershell
pip install -r requirements.txt
Copy-Item .env.example .env
# Edit .env with your API key
python read_bmw_data.py
python analyze_bmw_sales.py
start reports/BMW_Sales_Analysis_Report.html
```

### Regular Usage
```powershell
python analyze_bmw_sales.py
start reports/BMW_Sales_Analysis_Report.html
```

## 📁 Key Files

| File | Purpose |
|------|---------|
| `read_bmw_data.py` | Clean raw data |
| `analyze_bmw_sales.py` | Run full analysis |
| `.env` | Store API key |
| `requirements.txt` | Python packages |
| `reports/BMW_Sales_Analysis_Report.html` | View results |

## 🔑 Environment Variables (.env)

```
OPENAI_API_KEY=sk-your-key-here
OPENAI_MODEL=gpt-4
OPENAI_TEMPERATURE=0.7
```

Get API key: https://platform.openai.com/api-keys

## 📊 What Gets Generated

### Reports (in `reports/` folder)
- `BMW_Sales_Analysis_Report.html` - Main report
- `BMW_Sales_Analysis_Report.md` - Markdown version

### Charts (8 total)
1. Yearly sales trends
2. Regional performance  
3. Model performance
4. Price analysis
5. Fuel type trends
6. Revenue analysis
7. Correlation heatmap
8. Model category performance

### Cleaned Data
- `data-bmw/BMW sales data (2020-2024) Cleaned.xlsx`

## 📈 Analysis Sections

1. **Executive Summary** - High-level findings
2. **Key Metrics** - Dashboard of KPIs
3. **Yearly Trends** - 2020-2024 performance
4. **Regional Analysis** - Market performance
5. **Model Analysis** - Product insights
6. **Price Drivers** - Sales factors
7. **Creative Insights** - Unique findings
8. **Recommendations** - Action items

## ⚡ Typical Run Time

| Step | Time |
|------|------|
| Data cleaning | 10-30s |
| Analysis | <5s |
| Visualizations | 5-10s |
| LLM insights | 60-120s |
| Report generation | <5s |
| **Total** | **2-3 min** |

## 💰 Cost (OpenAI API)

| Model | Cost per Report |
|-------|----------------|
| GPT-4 | $0.30-$0.60 |
| GPT-3.5-turbo | $0.03-$0.06 |

## 🔧 Common Issues

| Problem | Solution |
|---------|----------|
| "API key not found" | Create `.env` file with `OPENAI_API_KEY=...` |
| "File not found" | Check file name: `BMW sales data (2020-2024).xlsx` |
| "Module not found" | Run `pip install -r requirements.txt` |
| "OpenAI error" | Check API key & credits at platform.openai.com |

## 📝 Module Overview

```
analyze_bmw_sales.py (main)
    ├── data_analyzer.py (statistics)
    ├── visualizer.py (charts)
    ├── llm_insights.py (AI insights)
    └── report_generator.py (HTML/MD)
```

## 🎯 Required Data Format

Excel file with columns:
- Model
- Year  
- Region
- Color
- Fuel_Type
- Transmission
- Engine_Size_L
- Mileage_KM
- Price_USD
- Sales_Volume

## 📚 Documentation

| File | Content |
|------|---------|
| `README.md` | Full documentation |
| `SETUP_GUIDE.md` | Step-by-step setup |
| `PROJECT_SUMMARY.md` | Technical overview |
| This file | Quick reference |

## 🌟 Pro Tips

1. Use GPT-3.5-turbo for faster/cheaper results
2. Run analysis after hours (API is faster)
3. Keep reports folder to compare runs
4. Backup your `.env` file (but don't commit it!)
5. Check OpenAI usage dashboard regularly

## 🆘 Getting Help

1. Check `SETUP_GUIDE.md` for setup issues
2. Review `README.md` for detailed docs
3. Verify all files in project structure exist
4. Ensure Python 3.12 is installed
5. Test internet connection for API calls

---

**Need more details?** See README.md  
**First time user?** See SETUP_GUIDE.md  
**Technical details?** See PROJECT_SUMMARY.md
