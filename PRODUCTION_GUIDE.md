# Production Deployment Guide

## Overview
This guide covers deploying the BMW Sales Analysis system in a production environment with best practices for reliability, monitoring, and maintenance.

## System Requirements

### Hardware
- **CPU**: 4+ cores recommended
- **RAM**: 8GB minimum, 16GB recommended
- **Storage**: 5GB free space minimum
- **Network**: Stable internet connection for API calls

### Software
- **Python**: 3.12+
- **Operating System**: Windows 10/11, Linux, or macOS
- **Dependencies**: See `requirements.txt`

## Pre-Deployment Checklist

### 1. Environment Configuration
```bash
# Copy and configure environment file
cp .env.example .env

# Edit .env with production API keys
# CRITICAL: Never commit .env to version control
```

### 2. API Key Management
- [ ] Obtain production API keys (OpenAI or Gemini)
- [ ] Store keys securely (use environment variables or secrets manager)
- [ ] Set appropriate rate limits and quotas
- [ ] Configure fallback providers if needed

### 3. Data Validation
- [ ] Verify data file format matches expectations
- [ ] Test with sample data first
- [ ] Validate data quality and completeness
- [ ] Ensure data path is accessible

### 4. Dependency Installation
```bash
# Install all required packages
pip install -r requirements.txt

# Verify installations
python -c "import pandas, openai, google.generativeai; print('OK')"
```

## Deployment Steps

### Step 1: Clone Repository
```bash
git clone https://github.com/timothyho12321/data-science-bmw-llm.git
cd data-science-bmw-llm
```

### Step 2: Configure Environment
```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Configure Settings
```bash
# Copy and edit environment file
cp .env.example .env

# Edit .env with your configuration:
# - LLM_PROVIDER (openai or gemini)
# - API keys
# - Model selection
# - Analysis role
```

### Step 4: Prepare Data
```bash
# Place data file in correct location
# data-bmw/BMW sales data (2020-2024).xlsx

# Run data cleaning
python read_bmw_data.py
```

### Step 5: Run Initial Test
```bash
# Run full analysis
python analyze_bmw_sales.py

# Check outputs in reports/ directory
# Review logs in logs/ directory
```

## Production Configuration

### Logging
```python
# Logging is automatically configured
# Logs are stored in: logs/bmw_analysis_YYYYMMDD.log

# Log levels:
# - DEBUG: Detailed information for debugging
# - INFO: General informational messages (console)
# - WARNING: Warning messages
# - ERROR: Error messages
# - CRITICAL: Critical errors
```

### Error Handling
The system includes comprehensive error handling:
- **Validation errors**: Configuration and data validation
- **API errors**: Graceful handling of LLM API failures
- **Data errors**: Invalid or missing data handling
- **Report generation errors**: Fallback mechanisms

### Monitoring
Monitor these key metrics:
1. **Execution time**: Track analysis duration
2. **API usage**: Monitor API call volume and costs
3. **Error rates**: Track failures and exceptions
4. **Report quality scores**: Monitor evaluation metrics

## Performance Optimization

### 1. API Cost Management
```bash
# Use cost-effective models for development
LLM_PROVIDER=gemini
GEMINI_MODEL=gemini-2.5-flash

# Use premium models for production
LLM_PROVIDER=openai
OPENAI_MODEL=gpt-4
```

### 2. Caching Strategy
- Cache analysis results for repeated runs
- Store intermediate data
- Reuse visualizations when data unchanged

### 3. Parallel Processing
Current implementation runs sequentially. For optimization:
- Parallelize visualization generation
- Batch API calls where possible
- Use async processing for independent tasks

## Quality Assurance

### Automated Testing
```bash
# Run report evaluation
python analyze_bmw_sales.py

# Check evaluation results in:
# reports/evaluations/evaluation_YYYYMMDD_HHMMSS.json
```

### Quality Metrics
- **Correctness**: ≥70% (data accuracy, logical coherence)
- **Completeness**: ≥70% (all sections present)
- **Readability**: ≥70% (proper formatting)
- **Data Quality**: ≥70% (valid, sufficient data)
- **Insight Quality**: ≥70% (specific, actionable)

### Manual Review
Periodically review:
- [ ] Generated reports for accuracy
- [ ] Insight relevance and actionability
- [ ] Visualization clarity
- [ ] Log files for errors or warnings

## Backup and Recovery

### Backup Strategy
```bash
# Backup configuration
cp .env .env.backup

# Backup reports
cp -r reports reports_backup_$(date +%Y%m%d)

# Backup logs
cp -r logs logs_backup_$(date +%Y%m%d)
```

### Recovery Procedures
1. **Configuration loss**: Restore from .env.backup
2. **Report failure**: Check logs, rerun analysis
3. **Data corruption**: Restore from cleaned data backup
4. **API failures**: Switch to fallback provider

## Maintenance

### Daily Tasks
- [ ] Check log files for errors
- [ ] Monitor API usage and costs
- [ ] Verify report generation

### Weekly Tasks
- [ ] Review evaluation scores
- [ ] Update dependencies if needed
- [ ] Clean old logs and reports

### Monthly Tasks
- [ ] Full system test with sample data
- [ ] Review and optimize performance
- [ ] Update documentation
- [ ] Security audit

## Security Best Practices

### 1. API Key Security
- Never commit API keys to version control
- Use environment variables or secrets manager
- Rotate keys regularly
- Set appropriate access controls

### 2. Data Privacy
- Ensure compliance with data protection regulations
- Implement data encryption if handling sensitive information
- Control access to reports and logs
- Audit data access

### 3. Access Control
- Implement user authentication if web-facing
- Use role-based access control
- Log all access attempts
- Regular security reviews

## Troubleshooting

### Common Issues

**Issue**: "API key not found"
```bash
# Solution: Check .env file exists and has correct key
cat .env | grep API_KEY
```

**Issue**: "Module not found"
```bash
# Solution: Reinstall dependencies
pip install -r requirements.txt --upgrade
```

**Issue**: "Data file not found"
```bash
# Solution: Verify data file location
ls -la "data-bmw/BMW sales data (2020-2024).xlsx"
```

**Issue**: "Low evaluation scores"
```bash
# Solution: Review evaluation report for specific issues
cat reports/evaluations/evaluation_report_*.txt
```

### Getting Help
1. Check logs in `logs/` directory
2. Review evaluation reports
3. Consult documentation
4. Check GitHub issues

## Scaling Considerations

### Horizontal Scaling
- Run multiple instances for different datasets
- Distribute API calls across instances
- Load balance if serving via API

### Vertical Scaling
- Increase memory for large datasets
- Add CPU cores for parallel processing
- Use faster storage (SSD)

### Cloud Deployment
Consider cloud platforms for:
- AWS: Lambda, ECS, or EC2
- Google Cloud: Cloud Run or Compute Engine
- Azure: Functions or App Service

## Monitoring and Alerts

### Key Metrics to Track
```python
# Example monitoring metrics
metrics = {
    'execution_time': '< 300 seconds',
    'api_calls': '< 50 per run',
    'error_rate': '< 5%',
    'evaluation_score': '≥ 80/100'
}
```

### Alert Triggers
Set up alerts for:
- Execution time > 10 minutes
- API failures > 3 consecutive
- Evaluation score < 70
- Critical errors in logs

## Compliance

### Data Protection
- GDPR compliance if processing EU data
- Data retention policies
- Right to deletion implementation
- Privacy impact assessments

### Audit Trail
- Log all data access
- Track report generation
- Monitor API usage
- Record configuration changes

## Support and Maintenance

### Documentation
- Keep README.md updated
- Document configuration changes
- Update troubleshooting guide
- Maintain changelog

### Version Control
```bash
# Tag stable releases
git tag -a v1.0.0 -m "Production release 1.0.0"
git push origin v1.0.0
```

### Updates
```bash
# Update dependencies
pip list --outdated
pip install -r requirements.txt --upgrade

# Test after updates
python analyze_bmw_sales.py
```

## Production Checklist

Before going live:
- [ ] All tests passing
- [ ] API keys configured and tested
- [ ] Logging enabled and working
- [ ] Monitoring configured
- [ ] Backup strategy in place
- [ ] Documentation complete
- [ ] Security audit completed
- [ ] Performance benchmarked
- [ ] Error handling tested
- [ ] Rollback plan prepared
