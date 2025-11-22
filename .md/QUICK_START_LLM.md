# Quick Reference: LLM Provider Configuration

## Switch Between Providers

### Use OpenAI GPT-4 (Best Quality)
```bash
LLM_PROVIDER=openai
OPENAI_API_KEY=your_key
OPENAI_MODEL=gpt-4
```
**Cost**: ~$0.30-$0.60/report | **Speed**: Medium

### Use OpenAI GPT-3.5-turbo (Fast & Affordable)
```bash
LLM_PROVIDER=openai
OPENAI_API_KEY=your_key
OPENAI_MODEL=gpt-3.5-turbo
```
**Cost**: ~$0.03-$0.06/report | **Speed**: Fast

### Use Gemini 1.5 Pro (Balanced)
```bash
LLM_PROVIDER=gemini
GEMINI_API_KEY=your_key
GEMINI_MODEL=gemini-1.5-pro
```
**Cost**: ~$0.02-$0.04/report | **Speed**: Fast

### Use Gemini 1.5 Flash (Most Cost-Effective)
```bash
LLM_PROVIDER=gemini
GEMINI_API_KEY=your_key
GEMINI_MODEL=gemini-1.5-flash
```
**Cost**: ~$0.01-$0.02/report | **Speed**: Very Fast

## Get API Keys

- **OpenAI**: https://platform.openai.com/api-keys
- **Gemini**: https://makersuite.google.com/app/apikey

## Analysis Modes

### Detailed Analysis (Default)
```bash
ROLE=Business Analyst
```
4-5 paragraph detailed analyses per section

### Executive Summary
```bash
ROLE=Business Chief
```
Concise BLUF-style strategic insights

## Complete Example Configuration

```bash
# Choose one provider
LLM_PROVIDER=gemini

# Gemini configuration
GEMINI_API_KEY=AIzaSyC_your_key_here
GEMINI_MODEL=gemini-1.5-flash

# Universal settings
LLM_TEMPERATURE=0.7
ROLE=Business Analyst
```

## Quick Command Reference

```powershell
# Install dependencies
pip install -r requirements.txt

# Clean data (first time only)
python read_bmw_data.py

# Run analysis
python analyze_bmw_sales.py
```

## Troubleshooting One-Liners

```powershell
# Check if provider module loads
python -c "from llm_provider import LLMProvider; print('OK')"

# Verify OpenAI package
python -c "import openai; print(f'OpenAI version: {openai.__version__}')"

# Verify Gemini package  
python -c "import google.generativeai as genai; print('Gemini package installed')"

# Test current configuration
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(f'Provider: {os.getenv(\"LLM_PROVIDER\", \"openai\")}'); print(f'Role: {os.getenv(\"ROLE\", \"Business Analyst\")}')"
```

## Cost Optimization Guide

| Scenario | Recommended Setup |
|----------|-------------------|
| Development/Testing | Gemini Flash |
| Regular Reports | GPT-3.5-turbo or Gemini Pro |
| Executive Presentations | GPT-4 |
| High-Volume Processing | Gemini Flash |
| Best Quality Needed | GPT-4 |

## Full Documentation

- **Setup**: README.md
- **Provider Guide**: LLM_PROVIDER_GUIDE.md
- **Implementation**: GEMINI_IMPLEMENTATION.md
