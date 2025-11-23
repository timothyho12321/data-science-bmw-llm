# BMW Sales Analysis - LLM-Powered Insights

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Production-grade BMW sales data analysis system powered by Large Language Models (OpenAI GPT-4 or Google Gemini). Generates comprehensive business insights, visualizations, and quality-assured reports with automated evaluation.

## 🎯 Features

### Core Capabilities
- **Automated Data Cleaning**: Removes duplicates, handles missing values, detects outliers
- **Statistical Analysis**: Comprehensive analysis of sales trends, regional performance, model performance
- **Professional Visualizations**: High-quality charts using matplotlib and seaborn
- **LLM-Powered Insights**: Supports OpenAI (GPT-4/GPT-3.5-turbo) and Google Gemini (2.5-flash/2.5-pro)
- **Multi-Provider Support**: Flexible provider switching via configuration
- **Role-Based Analysis**: Business Analyst (detailed) or Business Chief (strategic)
- **Automated Reporting**: Professional HTML and Markdown reports with embedded visualizations

### Production Features
- **Quality Evaluation**: 5-dimension automated quality assessment (correctness, completeness, readability, data quality, insight quality)
- **Comprehensive Logging**: Dual-handler system (DEBUG file logs + INFO console logs)
- **Error Handling**: Graceful error handling with detailed stack traces
- **Environment Validation**: API key and configuration validation
- **Execution Monitoring**: Timing and performance tracking
- **Modular Architecture**: Clean, well-documented, maintainable code
- **Test Suite**: >80% code coverage with unit and integration tests
- **Docker Support**: Containerized deployment for consistency
- **CI/CD Pipeline**: Automated testing and validation with GitHub Actions
- **Code Quality**: Black formatting, flake8 linting, type hints

## 📋 Requirements

- Python 3.12 or higher
- 8GB RAM minimum (16GB recommended)
- LLM API Key (OpenAI or Google Gemini)
- BMW sales data file: `data-bmw/BMW sales data (2020-2024).xlsx`
- Internet connection for LLM API calls

## 🚀 Quick Start

### Option 1: Docker (Recommended)

```bash
# Build and run
docker-compose up bmw-analysis

# View reports in reports/ directory
```

### Option 2: Local Installation

### 1. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 2. Configure Environment

Create a `.env` file in the project root:

```powershell
Copy-Item .env.example .env
```

Edit `.env` and configure your settings:

```env
# Choose your LLM provider
LLM_PROVIDER=gemini  # Options: openai, gemini

# If using OpenAI:
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4  # Options: gpt-4, gpt-3.5-turbo

# If using Google Gemini:
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-flash  # Options: gemini-2.5-flash, gemini-2.5-pro

# Analysis Settings
ROLE=Business Chief  # Options: Business Analyst, Business Chief
LLM_TEMPERATURE=0.7  # Range: 0.0-1.0

```

### 3. Run Analysis

```powershell
python analyze_bmw_sales.py
```

This will execute 6 steps:
1. **Environment Validation**: Check configuration and API keys
2. **Data Loading**: Read and validate BMW sales data
3. **Analysis & Visualization**: Generate charts and statistics
4. **LLM Insights**: Generate business insights (7 categories)
5. **Report Generation**: Create HTML and Markdown reports
6. **Quality Evaluation**: Assess report quality

### 4. View Results

- **HTML Report**: `reports/bmw_analysis_report_YYYYMMDD_HHMMSS.html`
- **Markdown Report**: `reports/bmw_analysis_report_YYYYMMDD_HHMMSS.md`
- **Evaluation**: `reports/evaluations/evaluation_report_YYYYMMDD_HHMMSS.txt`
- **Logs**: `logs/bmw_analysis_YYYYMMDD.log`

## 📊 Output Files

### Reports Directory
```
reports/
├── bmw_analysis_report_YYYYMMDD_HHMMSS.html    # Interactive HTML report
├── bmw_analysis_report_YYYYMMDD_HHMMSS.md      # Markdown report
└── evaluations/
    ├── evaluation_YYYYMMDD_HHMMSS.json         # Evaluation data (machine-readable)
    └── evaluation_report_YYYYMMDD_HHMMSS.txt   # Evaluation summary (human-readable)
```

### Logs Directory
```
logs/
└── bmw_analysis_YYYYMMDD.log                   # Detailed execution log (DEBUG level)
```

### Visualizations (embedded in reports)
1. Sales trends over time (line chart)
2. Top models by sales (bar chart)
3. Sales by region (horizontal bar chart)
4. Price distribution (histogram)
5. Correlation heatmap
6. Monthly sales patterns

## 🏆 Quality Evaluation

### Evaluation Framework

Reports are automatically evaluated across 5 dimensions:

1. **Correctness (0-100)**
   - Data consistency validation
   - Section completeness
   - Logical coherence
   - No negative/invalid values

2. **Completeness (0-100)**
   - All 7 insight categories present
   - Comprehensive coverage
   - Regional and model analysis
   - Correlation insights

3. **Readability (0-100)**
   - Proper file sizes (5KB-5MB)
   - Valid HTML structure
   - Clear formatting
   - Chart presence

4. **Data Quality (0-100)**
   - Sufficient dataset size (>1000 records)
   - Temporal coverage (≥2 years)
   - Balanced distribution
   - Valid value ranges

5. **Insight Quality (0-100)**
   - Adequate length (>200 characters)
   - Specific numbers/percentages
   - Actionable recommendations
   - Strategic relevance

### Scoring
- **Overall Score**: Average of 5 dimensions (0-100)
- **Letter Grades**: A (90+), B (80-89), C (70-79), D (60-69), F (<60)
- **Target**: ≥70 (passing) across all dimensions

### Example Evaluation Output
```
=== BMW Analysis Report Quality Evaluation ===

Overall Score: 85/100 (Grade: B)

Dimension Scores:
✓ Correctness:   92/100
✓ Completeness:  88/100
✓ Readability:   90/100
✓ Data Quality:  80/100
✓ Insight Quality: 75/100

Issues Found (3):
- Insight length below 200 chars in sales_trends
- Missing specific percentage in regional_analysis
- Could include more actionable recommendations
```

## 📝 Logging

### Log Configuration

Dual-handler logging system:

1. **File Logging** (DEBUG level)
   - Location: `logs/bmw_analysis_YYYYMMDD.log`
   - Detailed execution traces
   - Function entry/exit tracking
   - Exception stack traces

2. **Console Logging** (INFO level)
   - Step-by-step progress
   - Key milestones
   - Error summaries
   - Final results

### Viewing Logs

```powershell
# View latest log
Get-Content logs\bmw_analysis_*.log | Select-Object -Last 50

# Search for errors
Select-String -Path logs\*.log -Pattern "ERROR"
```

## 📈 Analysis Sections

The generated reports include 7 comprehensive insight categories:

1. **Sales Trends** - Patterns, seasonality, growth rates
2. **Model Performance** - Best/worst performers, market share
3. **Regional Analysis** - Geographic patterns, opportunities
4. **Price Analysis** - Pricing strategy, elasticity
5. **Customer Insights** - Demographics, preferences
6. **Recommendations** - Actionable business suggestions
7. **Overall Summary** - Executive overview

## 🧪 Testing

### Run Tests

```powershell
# All tests with coverage
pytest --cov=. --cov-report=html

# Or use Makefile
make test
```

### Code Quality

```powershell
# Linting
make lint

# Code formatting
make format
```

See [TESTING.md](TESTING.md) for complete testing guide.

## 🐳 Docker Deployment

### Quick Start

```powershell
# Build image
docker build -t bmw-sales-analysis:latest .

# Run with docker-compose
docker-compose up bmw-analysis
```

See [DOCKER.md](DOCKER.md) for complete Docker guide.

## 🏗️ Project Structure

```
data-science-bmw-llm/
├── data-bmw/
│   ├── BMW sales data (2020-2024).xlsx          # Raw data
│   └── BMW sales data (2020-2024) Cleaned.xlsx  # Cleaned data (generated)
├── reports/                                       # Generated reports
│   └── evaluations/                               # Quality evaluations
├── logs/                                          # Execution logs
├── tests/                                         # Test suite
│   ├── test_data_analyzer.py
│   ├── test_llm_provider.py
│   └── test_report_evaluator.py
├── analyze_bmw_sales.py                          # Main orchestrator
├── read_bmw_data.py                              # Data cleaning
├── llm_provider.py                               # Multi-provider abstraction
├── llm_insights.py                               # Business Analyst insights
├── llm_insights_executive.py                     # Executive insights
├── generate_html_report.py                       # HTML report generation
├── generate_markdown_report.py                   # Markdown report generation
├── logger_config.py                              # Logging configuration
├── report_evaluator.py                           # Quality evaluation
├── Dockerfile                                     # Docker container definition
├── docker-compose.yml                             # Docker orchestration
├── Makefile                                       # Build automation
├── setup.py                                       # Package configuration
├── pytest.ini                                     # Test configuration
├── requirements.txt                               # Dependencies
├── requirements-dev.txt                           # Development dependencies
├── .env                                          # Your configuration (not tracked)
├── .env.example                                  # Configuration template
└── README.md                                     # This file
```

## 🔧 Core Modules

### analyze_bmw_sales.py
Main orchestration script with 6 steps:
1. Environment validation
2. Data loading
3. Analysis and visualization
4. LLM insight generation
5. Report generation
6. Quality evaluation

### llm_provider.py
Multi-provider abstraction layer:
- Supports OpenAI (GPT-4, GPT-3.5-turbo)
- Supports Google Gemini (2.5-flash, 2.5-pro)
- Unified interface for both providers
- Dynamic provider switching via configuration

### logger_config.py
Centralized logging configuration:
- Dual-handler system (file DEBUG + console INFO)
- Daily log rotation
- Function call decorator
- Prevents duplicate handlers

### report_evaluator.py
Quality evaluation framework:
- 5-dimension scoring system
- JSON and text report generation
- Issue tracking and recommendations
- Letter grade assignment

## 🎨 Model Selection Guide

### OpenAI Models

**GPT-4**
- **Best for**: Highest quality insights, complex analysis
- **Speed**: ~30-60 seconds per report
- **Cost**: ~$0.30-$0.60 per report
- **Use when**: Quality is priority, budget allows

**GPT-3.5-turbo**
- **Best for**: Good quality, faster turnaround
- **Speed**: ~15-30 seconds per report  
- **Cost**: ~$0.03-$0.06 per report
- **Use when**: Need speed, cost efficiency

### Gemini Models

**gemini-2.5-flash** (Recommended)
- **Best for**: Cost-effective, fast analysis
- **Speed**: ~10-20 seconds per report
- **Cost**: ~$0.01-$0.02 per report
- **Use when**: High volume, budget conscious

**gemini-2.5-pro**
- **Best for**: High quality at lower cost than GPT-4
- **Speed**: ~20-40 seconds per report
- **Cost**: ~$0.05-$0.10 per report
- **Use when**: Balance quality and cost

## 🔧 Configuration Options

### Analysis Role

**Business Analyst** (detailed, technical)
- 4-5 paragraph analyses per section
- Detailed metrics and statistics
- Technical terminology
- Comprehensive coverage

**Business Chief** (strategic, executive)
- BLUF (Bottom Line Up Front) structure
- Strategic insights and frameworks
- BCG Matrix, Pareto analysis
- High-level recommendations

### Temperature Setting

- **0.0-0.3**: Deterministic, consistent, factual
- **0.4-0.7**: Balanced (recommended for business)
- **0.8-1.0**: Creative, exploratory, varied

## 🔒 Security

- Never commit `.env` file with API keys
- `.gitignore` configured to exclude sensitive files
- API keys loaded from environment variables only
- Validate API keys before use (no placeholder text)

## 🆘 Troubleshooting

### Common Issues

**Error: "API key not found"**
```powershell
# Check .env file exists
Test-Path .env

# Verify API key format
Get-Content .env | Select-String "API_KEY"

# Ensure no placeholder text
Get-Content .env | Select-String "your_"
```

**Error: "google-generativeai package not installed"**
```powershell
pip install google-generativeai>=0.3.0
python -c "import google.generativeai; print('OK')"
```

**Error: "404 Model not found" (Gemini)**
```env
# Update to correct model name in .env
# OLD: GEMINI_MODEL=gemini-1.5-flash
# NEW: GEMINI_MODEL=gemini-2.5-flash
```

**Error: "File not found"**
```powershell
# Verify data file location
Test-Path "data-bmw\BMW sales data (2020-2024).xlsx"

# Run data cleaning first
python read_bmw_data.py
```

**Error: "Module not found"**
```powershell
# Reinstall all dependencies
pip install -r requirements.txt --upgrade

# Verify Python version
python --version  # Should be 3.12+
```

**Low Evaluation Scores**
```powershell
# Review evaluation report
Get-Content reports\evaluations\evaluation_report_*.txt

# Common fixes:
# - Ensure sufficient data (>1000 records, 2+ years)
# - Verify all 7 insight sections generated
# - Check for negative or invalid values
# - Review logs for LLM API errors
```

### Debug Mode

Enable detailed console logging:
```python
# In logger_config.py, change console handler level
console_handler.setLevel(logging.DEBUG)
```

### Getting Help

1. **Check logs**: `logs/bmw_analysis_YYYYMMDD.log`
2. **Review evaluation**: `reports/evaluations/`
3. **Consult documentation**: See below
4. **GitHub Issues**: Report bugs or request features

## 📚 Documentation

### Complete Documentation Set
- **[README.md](README.md)** (this file): System overview, features, and usage guide
- **[ARCHITECTURE.md](ARCHITECTURE.md)**: System architecture and data flow diagrams
- **[PRODUCTION.md](PRODUCTION.md)**: Production deployment, monitoring, and maintenance
- **[DOCKER.md](DOCKER.md)**: Docker containerization and deployment guide
- **[TESTING.md](TESTING.md)**: Testing strategy and procedures
- **[SUPPLEMENTARY_INFO.md](SUPPLEMENTARY_INFO.md)**: Quick reference, troubleshooting, and additional tips

### Additional Resources
- Code contains comprehensive docstrings
- Example configurations in `.env.example`
- Evaluation framework in `report_evaluator.py`
- CI/CD pipeline in `.github/workflows/ci.yml`

## 🤝 Contributing

### Development Setup
```powershell
# Clone repository
git clone https://github.com/timothyho12321/data-science-bmw-llm.git
cd data-science-bmw-llm

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run tests
make test
```

### Code Style
- Follow PEP 8 guidelines
- Use type hints for function parameters
- Write comprehensive docstrings
- Use logging instead of print statements
- Include error handling with try-except
- Maintain >80% test coverage

### Pre-commit Checks
```powershell
# Install pre-commit hooks
pip install pre-commit
pre-commit install

# Run manually
make lint
make test
```

### Submitting Changes
1. Fork the repository
2. Create feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m "Add feature"`
4. Push to branch: `git push origin feature/your-feature`
5. Open Pull Request with description

## 📄 License

MIT License - see LICENSE file for details

## 🙏 Acknowledgments

- **OpenAI**: GPT models for natural language insights
- **Google**: Gemini models for cost-effective analysis  
- **Python Community**: Excellent data science libraries (pandas, matplotlib, seaborn)

## 📞 Contact

- **GitHub**: [@timothyho12321](https://github.com/timothyho12321)
- **Issues**: [GitHub Issues](https://github.com/timothyho12321/data-science-bmw-llm/issues)

## 🗺️ Roadmap

### Planned Features
- [ ] Automated scheduling for batch processing
- [ ] REST API for on-demand analysis
- [ ] Real-time monitoring dashboard
- [ ] Multi-language report generation
- [ ] Advanced forecasting models (ARIMA, Prophet)
- [ ] Custom evaluation criteria configuration
- [ ] Report comparison across time periods
- [ ] Cloud deployment templates (AWS, GCP, Azure)

### Recent Updates
- **v1.0.0** (2024-01): Production-grade release
  - Multi-provider LLM support (OpenAI + Gemini)
  - Quality evaluation framework (5 dimensions)
  - Comprehensive logging (DEBUG file + INFO console)
  - Test suite with >80% coverage
  - Docker containerization
  - CI/CD pipeline with GitHub Actions
  - Code quality tools and automation
  - Production documentation and deployment guide
  - Environment validation and error handling

---

**Built with ❤️ for data-driven business insights**
