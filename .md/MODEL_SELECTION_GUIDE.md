# Model Selection Guide

## Switching Between GPT-4 and GPT-3.5-turbo

The system supports both OpenAI GPT-4 and GPT-3.5-turbo models. You can easily switch between them by editing your `.env` file.

## Quick Comparison

| Feature | GPT-4 | GPT-3.5-turbo |
|---------|-------|---------------|
| **Quality** | Highest quality insights | Good quality insights |
| **Detail** | More comprehensive analysis | Concise analysis |
| **Speed** | Slower (~15-20s per insight) | Faster (~8-12s per insight) |
| **Cost per Report** | $0.30 - $0.60 | $0.03 - $0.06 |
| **Best For** | Final reports, presentations | Development, testing, frequent runs |

## How to Switch Models

### Option 1: Edit .env file

Open your `.env` file and change the `OPENAI_MODEL` line:

**For GPT-4 (default):**
```
OPENAI_MODEL=gpt-4
```

**For GPT-3.5-turbo (faster/cheaper):**
```
OPENAI_MODEL=gpt-3.5-turbo
```

### Option 2: Use Different Model Variants

You can also use specific model versions:

```
# Latest GPT-4
OPENAI_MODEL=gpt-4-turbo-preview

# Standard GPT-4
OPENAI_MODEL=gpt-4

# GPT-3.5-turbo (16k context)
OPENAI_MODEL=gpt-3.5-turbo-16k

# Standard GPT-3.5
OPENAI_MODEL=gpt-3.5-turbo
```

## When to Use Each Model

### Use GPT-4 when:
✅ Creating final reports for stakeholders  
✅ Need maximum insight quality and depth  
✅ Presenting to executives or clients  
✅ Budget is not a primary concern  
✅ Complex business scenarios require nuanced analysis

### Use GPT-3.5-turbo when:
✅ Testing and development  
✅ Running analysis frequently  
✅ Working with limited budget  
✅ Need faster results  
✅ Quality is good enough for internal use

## Cost Estimation

### Per Report Cost Breakdown

**GPT-4:**
- 7 API calls per report
- ~15,000-20,000 total tokens
- Input: ~$0.01 per 1K tokens
- Output: ~$0.03 per 1K tokens
- **Total: $0.30-$0.60 per report**

**GPT-3.5-turbo:**
- 7 API calls per report
- ~15,000-20,000 total tokens
- Input: ~$0.0015 per 1K tokens
- Output: ~$0.002 per 1K tokens
- **Total: $0.03-$0.06 per report**

### Monthly Cost Example

If you run the analysis **10 times per month**:

| Model | Cost per Run | Monthly Cost |
|-------|--------------|--------------|
| GPT-4 | $0.45 | **$4.50** |
| GPT-3.5-turbo | $0.045 | **$0.45** |

## Switching Models on the Fly

You can also override the model temporarily without editing `.env`:

### Windows PowerShell:
```powershell
$env:OPENAI_MODEL="gpt-3.5-turbo"
python analyze_bmw_sales.py
```

### Linux/Mac:
```bash
export OPENAI_MODEL="gpt-3.5-turbo"
python analyze_bmw_sales.py
```

## Verification

When you run `python analyze_bmw_sales.py`, the system will display which model is being used:

```
Step 4: Generating LLM-powered insights...
--------------------------------------------------------------------------------
Using OpenAI model: gpt-4
  → Using GPT-4 (higher quality, more detailed insights)
```

or

```
Step 4: Generating LLM-powered insights...
--------------------------------------------------------------------------------
Using OpenAI model: gpt-3.5-turbo
  → Using GPT-3.5-turbo (faster, more cost-effective)
```

## Best Practice Recommendation

**Development workflow:**
1. Use **GPT-3.5-turbo** for initial testing and development
2. Run multiple iterations to refine prompts and analysis
3. Switch to **GPT-4** for final production reports

This approach balances cost and quality effectively.

## Quality Comparison

Both models will provide:
- ✅ Executive summaries
- ✅ Trend analysis
- ✅ Performance insights
- ✅ Strategic recommendations

**GPT-4 advantages:**
- More nuanced understanding of business context
- Better at connecting disparate data points
- More sophisticated strategic recommendations
- Better handling of complex scenarios

**GPT-3.5-turbo advantages:**
- 10x cheaper
- 30-40% faster
- Still produces professional-quality reports
- Great for iterative development

## Troubleshooting

### "Model not found" error
Make sure you're using a valid model name:
- `gpt-4`
- `gpt-4-turbo-preview`
- `gpt-3.5-turbo`
- `gpt-3.5-turbo-16k`

### API rate limits
If you hit rate limits with GPT-4, switch to GPT-3.5-turbo which has higher rate limits.

### Cost concerns
Monitor your usage at: https://platform.openai.com/account/usage

## Example .env Configuration

```env
# OpenAI API Configuration
OPENAI_API_KEY=sk-your-actual-key-here

# Choose your model (gpt-4 or gpt-3.5-turbo)
OPENAI_MODEL=gpt-3.5-turbo

# Temperature (0.0-1.0)
OPENAI_TEMPERATURE=0.7
```

Save the file and run your analysis - that's it! The system will automatically use your selected model.
