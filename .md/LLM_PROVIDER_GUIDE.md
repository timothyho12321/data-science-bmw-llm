# LLM Provider Guide

## Overview

The BMW Sales Analysis system supports multiple LLM providers, giving you flexibility in choosing the AI model that best fits your needs in terms of quality, speed, and cost.

## Supported Providers

### 1. OpenAI (GPT Models)
- **Models**: GPT-4, GPT-3.5-turbo
- **Best for**: High-quality insights, complex analysis
- **API Key**: Get from [OpenAI Platform](https://platform.openai.com/api-keys)

### 2. Google Gemini
- **Models**: Gemini 1.5 Pro, Gemini 1.5 Flash
- **Best for**: Fast, cost-effective analysis
- **API Key**: Get from [Google AI Studio](https://makersuite.google.com/app/apikey)

## Configuration

### Using OpenAI

In your `.env` file:

```bash
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-your-openai-api-key-here
OPENAI_MODEL=gpt-4
LLM_TEMPERATURE=0.7
```

**Available Models:**
- `gpt-4` - Best quality, most detailed insights
- `gpt-3.5-turbo` - Faster, more economical

### Using Google Gemini

In your `.env` file:

```bash
LLM_PROVIDER=gemini
GEMINI_API_KEY=your-gemini-api-key-here
GEMINI_MODEL=gemini-1.5-flash
LLM_TEMPERATURE=0.7
```

**Available Models:**
- `gemini-1.5-pro` - Best quality, balanced performance
- `gemini-1.5-flash` - Fastest, most cost-effective

## Model Comparison

| Provider | Model | Quality | Speed | Cost (per report) | Best Use Case |
|----------|-------|---------|-------|-------------------|---------------|
| OpenAI | GPT-4 | ⭐⭐⭐⭐⭐ | 🐌 Medium | $0.30-$0.60 | Executive reports, detailed analysis |
| OpenAI | GPT-3.5-turbo | ⭐⭐⭐⭐ | 🚀 Fast | $0.03-$0.06 | Regular analysis, quick insights |
| Gemini | Gemini 1.5 Pro | ⭐⭐⭐⭐ | 🚀 Fast | $0.02-$0.04 | Balanced quality and cost |
| Gemini | Gemini 1.5 Flash | ⭐⭐⭐ | ⚡ Very Fast | $0.01-$0.02 | High-volume processing, rapid iteration |

## Switching Providers

Simply update your `.env` file and change the `LLM_PROVIDER` variable:

```bash
# From OpenAI to Gemini
LLM_PROVIDER=gemini

# From Gemini to OpenAI
LLM_PROVIDER=openai
```

No code changes required! The system automatically uses the appropriate provider.

## Cost Optimization Tips

### For Development/Testing
Use the most cost-effective options:
```bash
LLM_PROVIDER=gemini
GEMINI_MODEL=gemini-1.5-flash
```

### For Production Reports
Use higher quality models:
```bash
LLM_PROVIDER=openai
OPENAI_MODEL=gpt-4
```

### For High-Volume Processing
Balance cost and quality:
```bash
LLM_PROVIDER=gemini
GEMINI_MODEL=gemini-1.5-pro
```

## Temperature Settings

The `LLM_TEMPERATURE` parameter controls creativity vs. consistency:

- **0.0-0.3**: Very deterministic, consistent outputs (good for formal reports)
- **0.4-0.7**: Balanced (recommended for most uses)
- **0.8-1.0**: More creative, varied insights (good for brainstorming)

**Recommended:**
```bash
LLM_TEMPERATURE=0.7
```

## Getting API Keys

### OpenAI
1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign up or log in
3. Navigate to API Keys section
4. Click "Create new secret key"
5. Copy the key (starts with `sk-`)

### Google Gemini
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Select or create a Google Cloud project
5. Copy the generated API key

## Troubleshooting

### "API key not found" Error
- Ensure `.env` file exists in project root
- Verify the API key variable name matches the provider:
  - OpenAI: `OPENAI_API_KEY`
  - Gemini: `GEMINI_API_KEY`

### "Unsupported LLM_PROVIDER" Error
- Check `LLM_PROVIDER` value is either `openai` or `gemini` (lowercase)

### Package Import Errors
Install the required package:
```powershell
# For OpenAI
pip install openai>=1.0.0

# For Gemini
pip install google-generativeai>=0.3.0

# Or install all:
pip install -r requirements.txt
```

### Rate Limiting
If you hit API rate limits:
- OpenAI: Upgrade your account tier or wait
- Gemini: Check your quota at [Google Cloud Console](https://console.cloud.google.com/)

## Best Practices

1. **Start with cost-effective models** (Gemini Flash or GPT-3.5-turbo) during development
2. **Use higher-quality models** (GPT-4 or Gemini Pro) for final production reports
3. **Keep API keys secure** - never commit `.env` file to version control
4. **Monitor costs** - track your API usage in respective dashboards
5. **Test both providers** - different models may provide unique insights

## Provider-Specific Features

### OpenAI
- More established, widely used
- Excellent for complex reasoning
- Strong performance on business analysis
- Better documentation and community support

### Google Gemini
- Newer technology, rapidly improving
- Excellent cost-performance ratio
- Fast processing speeds
- Integrated with Google Cloud ecosystem

## Example Configurations

### Budget-Conscious Setup
```bash
LLM_PROVIDER=gemini
GEMINI_API_KEY=your_key_here
GEMINI_MODEL=gemini-1.5-flash
LLM_TEMPERATURE=0.7
ROLE=Business Analyst
```

### Premium Quality Setup
```bash
LLM_PROVIDER=openai
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-4
LLM_TEMPERATURE=0.7
ROLE=Business Chief
```

### Balanced Setup
```bash
LLM_PROVIDER=gemini
GEMINI_API_KEY=your_key_here
GEMINI_MODEL=gemini-1.5-pro
LLM_TEMPERATURE=0.7
ROLE=Business Analyst
```

## Support

For provider-specific issues:
- OpenAI: [OpenAI Help Center](https://help.openai.com/)
- Gemini: [Google AI Documentation](https://ai.google.dev/docs)

For system-specific issues, check the main README.md and TROUBLESHOOTING.md files.
