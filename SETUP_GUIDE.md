# Quick Setup Guide

## Step-by-Step Instructions

### 1. Install Required Packages
```powershell
pip install -r requirements.txt
```

### 2. Set Up Your OpenAI API Key

**Option A: Copy the example file**
```powershell
Copy-Item .env.example .env
```

**Option B: Create manually**
Create a file named `.env` in the project root with:
```
OPENAI_API_KEY=sk-your-actual-key-here
OPENAI_MODEL=gpt-4
OPENAI_TEMPERATURE=0.7
```

**Where to get an API key:**
- Go to: https://platform.openai.com/api-keys
- Sign up or log in
- Click "Create new secret key"
- Copy the key (starts with `sk-`)
- Paste it in your `.env` file

### 3. Place Your Data File

Ensure your BMW sales data file is located at:
```
data-bmw/BMW sales data (2020-2024).xlsx
```

The file should have these columns:
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

### 4. Clean the Data
```powershell
python read_bmw_data.py
```

**Expected output:**
- Data loaded and analyzed
- Cleaned data saved to: `data-bmw/BMW sales data (2020-2024) Cleaned.xlsx`
- Summary of cleaning operations

### 5. Run the Analysis
```powershell
python analyze_bmw_sales.py
```

**Expected output:**
- Statistical analysis complete
- 8 visualizations generated
- LLM insights generated (this may take 1-2 minutes)
- HTML and Markdown reports created

### 6. View Your Report

Open the HTML report in your browser:
```powershell
start reports/BMW_Sales_Analysis_Report.html
```

Or navigate to: `reports/BMW_Sales_Analysis_Report.html`

## Expected Timeline

- **Step 1 (Install):** 1-2 minutes
- **Step 2 (Setup):** 1 minute
- **Step 3 (Data):** Already provided
- **Step 4 (Clean):** 10-30 seconds
- **Step 5 (Analyze):** 1-3 minutes (depends on API response time)
- **Step 6 (View):** Instant

**Total time:** ~5-10 minutes

## Troubleshooting

### "pip: command not found"
- Make sure Python is installed
- Try: `python -m pip install -r requirements.txt`

### "OPENAI_API_KEY not found"
- Double-check your `.env` file exists
- Ensure it's in the project root directory
- Verify the API key is correct (no extra spaces)

### "File not found: BMW sales data"
- Check the file name is exactly: `BMW sales data (2020-2024).xlsx`
- Ensure it's in the `data-bmw/` folder
- Check for any extra spaces in the filename

### "OpenAI API error"
- Verify your API key is valid
- Check you have available credits at: https://platform.openai.com/account/usage
- Try using gpt-3.5-turbo instead (cheaper): Set `OPENAI_MODEL=gpt-3.5-turbo` in `.env`

### Reports not generating
- Make sure Step 4 (data cleaning) completed successfully
- Check that `BMW sales data (2020-2024) Cleaned.xlsx` exists in `data-bmw/` folder

## Cost Estimation

Using OpenAI GPT-4:
- Approximately 7 API calls per run
- ~15,000-20,000 tokens total
- Estimated cost: $0.30-$0.60 per report

Using GPT-3.5-turbo (alternative):
- Set `OPENAI_MODEL=gpt-3.5-turbo` in `.env`
- Estimated cost: $0.03-$0.06 per report

## What You'll Get

✅ **Professional HTML Report** with:
- Executive summary
- Key performance metrics dashboard
- 8 professional visualizations
- Detailed analysis sections
- Strategic recommendations
- Creative business insights

✅ **Markdown Report** for documentation

✅ **8 High-Quality Charts:**
1. Yearly sales trends
2. Regional performance
3. Model performance comparison
4. Price analysis
5. Fuel type trends
6. Revenue breakdown
7. Correlation heatmap
8. Model category performance

## Need Help?

Check the main README.md for detailed documentation.
