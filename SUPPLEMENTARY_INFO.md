# Supplementary Information

## Quick Start Guide

### First-Time Setup
```powershell
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure environment
Copy-Item .env.example .env
# Edit .env with your API key and settings

# 3. Run analysis
python analyze_bmw_sales.py
```

### Expected Timeline
- **Installation**: 1-2 minutes
- **Configuration**: 1 minute
- **Analysis execution**: 2-5 minutes
- **Total**: ~5-10 minutes

## LLM Provider Configuration

### Quick Reference

#### Use Google Gemini (Recommended - Fast & Cost-Effective)
```env
LLM_PROVIDER=gemini
GEMINI_API_KEY=your_key_here
GEMINI_MODEL=gemini-2.5-flash
```
**Cost**: ~$0.01-$0.02/report | **Speed**: Very Fast

#### Use OpenAI GPT-4 (Best Quality)
```env
LLM_PROVIDER=openai
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-4
```
**Cost**: ~$0.30-$0.60/report | **Speed**: Medium

#### Use OpenAI GPT-3.5-turbo (Balanced)
```env
LLM_PROVIDER=openai
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-3.5-turbo
```
**Cost**: ~$0.03-$0.06/report | **Speed**: Fast

### Get API Keys
- **OpenAI**: https://platform.openai.com/api-keys
- **Gemini**: https://makersuite.google.com/app/apikey

### Model Comparison

| Provider | Model | Quality | Speed | Cost/Report | Best For |
|----------|-------|---------|-------|-------------|----------|
| Gemini | 2.5-flash | ⭐⭐⭐ | ⚡ Very Fast | $0.01-$0.02 | Development, high-volume |
| Gemini | 2.5-pro | ⭐⭐⭐⭐ | 🚀 Fast | $0.05-$0.10 | Balanced quality/cost |
| OpenAI | GPT-3.5-turbo | ⭐⭐⭐⭐ | 🚀 Fast | $0.03-$0.06 | Regular analysis |
| OpenAI | GPT-4 | ⭐⭐⭐⭐⭐ | 🐌 Medium | $0.30-$0.60 | Executive reports |

### Analysis Modes

**Business Analyst** (Detailed)
```env
ROLE=Business Analyst
```
- 4-5 paragraph analyses per section
- Detailed metrics and statistics
- Technical terminology
- Comprehensive coverage

**Business Chief** (Strategic)
```env
ROLE=Business Chief
```
- BLUF (Bottom Line Up Front) structure
- Strategic insights and frameworks
- High-level recommendations
- Executive summary focus

### Temperature Settings

```env
LLM_TEMPERATURE=0.7  # Recommended
```
- **0.0-0.3**: Deterministic, consistent, factual
- **0.4-0.7**: Balanced (recommended)
- **0.8-1.0**: Creative, exploratory, varied

## Troubleshooting Guide

### Common Issues & Solutions

#### "API key not found"
```powershell
# Check .env file exists
Test-Path .env

# Verify API key
Get-Content .env | Select-String "API_KEY"

# Ensure no placeholder text
Get-Content .env | Select-String "your_"
```

#### "google-generativeai package not installed"
```powershell
pip install google-generativeai>=0.3.0
python -c "import google.generativeai; print('OK')"
```

#### "404 Model not found" (Gemini)
Update model name in .env:
```env
# OLD: GEMINI_MODEL=gemini-1.5-flash (deprecated)
# NEW: GEMINI_MODEL=gemini-2.5-flash
```

#### "Module not found"
```powershell
pip install -r requirements.txt --upgrade
python --version  # Should be 3.12+
```

#### "Low evaluation scores"
```powershell
# Review evaluation report
Get-Content reports\evaluations\evaluation_report_*.txt

# Common fixes:
# - Ensure sufficient data (>1000 records, 2+ years)
# - Verify all 7 insight sections generated
# - Check for negative or invalid values
# - Review logs for API errors
```

### Debug Mode

Enable detailed console logging by editing `logger_config.py`:
```python
console_handler.setLevel(logging.DEBUG)
```

### Testing Provider Configuration

```powershell
# Check provider module
python -c "from llm_provider import LLMProvider; print('OK')"

# Verify OpenAI
python -c "import openai; print(f'OpenAI: {openai.__version__}')"

# Verify Gemini
python -c "import google.generativeai as genai; print('Gemini: OK')"

# Test configuration
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(f'Provider: {os.getenv(\"LLM_PROVIDER\", \"openai\")}'); print(f'Role: {os.getenv(\"ROLE\", \"Business Analyst\")}')"
```

## Cost Optimization

### Recommended Setups by Scenario

| Scenario | Provider | Model | Rationale |
|----------|----------|-------|-----------|
| Development/Testing | Gemini | 2.5-flash | Fastest, cheapest |
| Regular Reports | OpenAI | GPT-3.5-turbo | Good balance |
| High-Volume Processing | Gemini | 2.5-flash | Cost-effective |
| Executive Presentations | OpenAI | GPT-4 | Best quality |
| Balanced Production | Gemini | 2.5-pro | Quality + cost |

### Monthly Cost Estimates

**Running 10 reports/month:**
- Gemini 2.5-flash: $0.15
- GPT-3.5-turbo: $0.45
- Gemini 2.5-pro: $0.75
- GPT-4: $4.50

**Running 100 reports/month:**
- Gemini 2.5-flash: $1.50
- GPT-3.5-turbo: $4.50
- Gemini 2.5-pro: $7.50
- GPT-4: $45.00

## Quick Reference Commands

### Regular Usage
```powershell
# Run analysis
python analyze_bmw_sales.py

# View HTML report
start reports\bmw_analysis_report_*.html

# View logs
Get-Content logs\bmw_analysis_*.log | Select-Object -Last 50

# View evaluation
Get-Content reports\evaluations\evaluation_report_*.txt
```

### Maintenance
```powershell
# Update dependencies
pip install -r requirements.txt --upgrade

# Clean old reports (keep last 10)
Get-ChildItem reports\bmw_*.html | Sort-Object CreationTime -Descending | Select-Object -Skip 10 | Remove-Item

# Clean old logs (older than 30 days)
Get-ChildItem logs\*.log | Where-Object {$_.CreationTime -lt (Get-Date).AddDays(-30)} | Remove-Item

# Backup configuration
Copy-Item .env .env.backup
```

## Key File Locations

| File/Directory | Purpose |
|----------------|---------|
| `.env` | Configuration (API keys, provider, model) |
| `analyze_bmw_sales.py` | Main orchestrator script |
| `reports/` | Generated HTML/Markdown reports |
| `reports/evaluations/` | Quality evaluation reports |
| `logs/` | Detailed execution logs |
| `data-bmw/` | Input data (raw and cleaned) |

## Required Data Format

Excel file with these columns:
- `Model` - Vehicle model name
- `Year` - Sales year (2020-2024)
- `Region` - Geographic region
- `Color` - Vehicle color
- `Fuel_Type` - Fuel type (Electric, Petrol, Diesel, Hybrid)
- `Transmission` - Automatic or Manual
- `Engine_Size_L` - Engine size in liters
- `Mileage_KM` - Mileage in kilometers
- `Price_USD` - Price in US dollars
- `Sales_Volume` - Number of units sold

## Module Overview

```
analyze_bmw_sales.py (main orchestrator)
    ├── read_bmw_data.py (data cleaning)
    ├── llm_provider.py (multi-provider abstraction)
    ├── llm_insights.py (Business Analyst insights)
    ├── llm_insights_executive.py (Business Chief insights)
    ├── generate_html_report.py (HTML generation)
    ├── generate_markdown_report.py (Markdown generation)
    ├── logger_config.py (logging setup)
    └── report_evaluator.py (quality assessment)
```

## Output Structure

```
reports/
├── bmw_analysis_report_YYYYMMDD_HHMMSS.html
├── bmw_analysis_report_YYYYMMDD_HHMMSS.md
└── evaluations/
    ├── evaluation_YYYYMMDD_HHMMSS.json
    └── evaluation_report_YYYYMMDD_HHMMSS.txt

logs/
└── bmw_analysis_YYYYMMDD.log
```

## Pro Tips

1. **Use Gemini 2.5-flash for development** - 10x cheaper than GPT-4
2. **Enable DEBUG logging** for detailed troubleshooting
3. **Review evaluation reports** to ensure quality ≥70
4. **Keep .env backed up** but never commit to version control
5. **Monitor API usage** through provider dashboards
6. **Test configuration changes** with small datasets first
7. **Archive old reports** to save disk space
8. **Switch providers** if one has rate limit issues

## Security Best Practices

- ✅ Never commit `.env` to version control
- ✅ Rotate API keys regularly (every 90 days)
- ✅ Use environment-specific API keys (dev vs prod)
- ✅ Set appropriate rate limits on API keys
- ✅ Monitor API usage for anomalies
- ✅ Restrict file permissions on `.env` file
- ✅ Use secrets manager for production deployments

## Additional Resources

- **OpenAI Documentation**: https://platform.openai.com/docs
- **Gemini Documentation**: https://ai.google.dev/docs
- **Python dotenv**: https://pypi.org/project/python-dotenv/
- **Pandas Documentation**: https://pandas.pydata.org/docs/

## Getting Help

1. Check this supplementary info first
2. Review logs in `logs/` directory
3. Check evaluation reports for quality issues
4. Consult README.md for comprehensive documentation
5. Review PRODUCTION.md for deployment guidance
6. Check ARCHITECTURE.md for system design

## Version History

- **v1.0.0** (2024-01): Production-grade release
  - Multi-provider LLM support (OpenAI + Gemini)
  - Quality evaluation framework (5 dimensions)
  - Comprehensive logging (DEBUG file + INFO console)
  - Environment validation and error handling
  - Production documentation

---

**For detailed system information, see README.md**  
**For deployment guidance, see PRODUCTION.md**  
**For system architecture, see ARCHITECTURE.md**
