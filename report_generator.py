"""
Report Generation Module
Creates professional HTML and Markdown reports combining analysis, visualizations, and LLM insights
"""

import os
from datetime import datetime
from typing import Dict, List, Any
import json


class ReportGenerator:
    """Generates comprehensive reports in HTML and Markdown formats"""
    
    def __init__(self, output_dir: str = "reports"):
        """
        Initialize report generator
        
        Parameters:
        -----------
        output_dir : str
            Directory to save generated reports
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def generate_html_report(self, 
                            analysis_data: Dict[str, Any],
                            llm_insights: Dict[str, str],
                            plot_files: List[str]) -> str:
        """
        Generate comprehensive HTML report
        
        Parameters:
        -----------
        analysis_data : dict
            Statistical analysis data
        llm_insights : dict
            LLM-generated insights
        plot_files : list
            List of plot file paths
            
        Returns:
        --------
        str : Path to generated HTML report
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BMW Sales Analysis Report (2020-2024)</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f5f5f5;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 40px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }}
        
        header {{
            text-align: center;
            padding-bottom: 30px;
            border-bottom: 3px solid #1c69d4;
            margin-bottom: 40px;
        }}
        
        h1 {{
            color: #1c69d4;
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .subtitle {{
            color: #666;
            font-size: 1.2em;
            margin-bottom: 5px;
        }}
        
        .timestamp {{
            color: #999;
            font-size: 0.9em;
            font-style: italic;
        }}
        
        h2 {{
            color: #1c69d4;
            font-size: 1.8em;
            margin-top: 40px;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #e0e0e0;
        }}
        
        h3 {{
            color: #333;
            font-size: 1.3em;
            margin-top: 30px;
            margin-bottom: 15px;
        }}
        
        p {{
            margin-bottom: 15px;
            text-align: justify;
        }}
        
        .executive-summary {{
            background-color: #f0f7ff;
            padding: 25px;
            border-left: 5px solid #1c69d4;
            margin: 30px 0;
            border-radius: 5px;
        }}
        
        .key-metrics {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }}
        
        .metric-card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        
        .metric-card h4 {{
            font-size: 0.9em;
            margin-bottom: 10px;
            opacity: 0.9;
        }}
        
        .metric-card .value {{
            font-size: 2em;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        
        .metric-card .label {{
            font-size: 0.85em;
            opacity: 0.8;
        }}
        
        .visualization {{
            margin: 30px 0;
            text-align: center;
        }}
        
        .visualization img {{
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
        
        .visualization-caption {{
            margin-top: 10px;
            font-style: italic;
            color: #666;
            font-size: 0.9em;
        }}
        
        .insight-box {{
            background-color: #fff9e6;
            border-left: 5px solid #ffa500;
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
        }}
        
        .recommendation-box {{
            background-color: #e6f7e6;
            border-left: 5px solid #28a745;
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
        }}
        
        .data-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        .data-table th {{
            background-color: #1c69d4;
            color: white;
            padding: 12px;
            text-align: left;
        }}
        
        .data-table td {{
            padding: 10px 12px;
            border-bottom: 1px solid #e0e0e0;
        }}
        
        .data-table tr:hover {{
            background-color: #f5f5f5;
        }}
        
        footer {{
            margin-top: 60px;
            padding-top: 20px;
            border-top: 2px solid #e0e0e0;
            text-align: center;
            color: #666;
            font-size: 0.9em;
        }}
        
        .toc {{
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 8px;
            margin: 30px 0;
        }}
        
        .toc h3 {{
            margin-top: 0;
            color: #1c69d4;
        }}
        
        .toc ul {{
            list-style-type: none;
            padding-left: 20px;
        }}
        
        .toc li {{
            margin: 8px 0;
        }}
        
        .toc a {{
            color: #1c69d4;
            text-decoration: none;
        }}
        
        .toc a:hover {{
            text-decoration: underline;
        }}
        
        @media print {{
            body {{
                background-color: white;
            }}
            .container {{
                box-shadow: none;
                padding: 20px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>BMW Sales Analysis Report</h1>
            <p class="subtitle">Comprehensive Analysis of Sales Performance (2020-2024)</p>
            <p class="timestamp">Generated on {timestamp}</p>
        </header>
        
        <div class="toc">
            <h3>Table of Contents</h3>
            <ul>
                <li><a href="#executive-summary">Executive Summary</a></li>
                <li><a href="#key-metrics">Key Performance Metrics</a></li>
                <li><a href="#yearly-trends">Yearly Sales Trends</a></li>
                <li><a href="#regional-performance">Regional Performance Analysis</a></li>
                <li><a href="#model-performance">Model Performance Analysis</a></li>
                <li><a href="#price-drivers">Price Drivers and Market Dynamics</a></li>
                <li><a href="#creative-insights">Creative Business Insights</a></li>
                <li><a href="#recommendations">Strategic Recommendations</a></li>
            </ul>
        </div>
        
        <section id="executive-summary">
            <h2>Executive Summary</h2>
            <div class="executive-summary">
                {self._format_text_with_paragraphs(llm_insights['executive_summary'])}
            </div>
        </section>
        
        <section id="key-metrics">
            <h2>Key Performance Metrics</h2>
            <div class="key-metrics">
                <div class="metric-card">
                    <h4>Total Sales Volume</h4>
                    <div class="value">{analysis_data['overview']['total_sales_volume']:,}</div>
                    <div class="label">Units Sold</div>
                </div>
                <div class="metric-card">
                    <h4>Average Price</h4>
                    <div class="value">${analysis_data['overview']['avg_price']:,.0f}</div>
                    <div class="label">Per Unit</div>
                </div>
                <div class="metric-card">
                    <h4>Total Models</h4>
                    <div class="value">{analysis_data['overview']['total_models']}</div>
                    <div class="label">Product Lines</div>
                </div>
                <div class="metric-card">
                    <h4>Global Regions</h4>
                    <div class="value">{analysis_data['overview']['total_regions']}</div>
                    <div class="label">Markets Served</div>
                </div>
            </div>
        </section>
        
        <section id="yearly-trends">
            <h2>Yearly Sales Trends</h2>
            {self._format_text_with_paragraphs(llm_insights['yearly_analysis'])}
            
            <div class="visualization">
                <img src="{os.path.basename(plot_files[0])}" alt="Yearly Sales Trends">
                <p class="visualization-caption">Figure 1: Sales volume and average price trends over time (2020-2024)</p>
            </div>
        </section>
        
        <section id="regional-performance">
            <h2>Regional Performance Analysis</h2>
            {self._format_text_with_paragraphs(llm_insights['regional_analysis'])}
            
            <div class="visualization">
                <img src="{os.path.basename(plot_files[1])}" alt="Regional Performance">
                <p class="visualization-caption">Figure 2: Sales performance and market share by region</p>
            </div>
            
            <h3>Regional Sales Breakdown</h3>
            {self._create_regional_table(analysis_data['regional_performance'])}
        </section>
        
        <section id="model-performance">
            <h2>Model Performance Analysis</h2>
            {self._format_text_with_paragraphs(llm_insights['model_analysis'])}
            
            <div class="visualization">
                <img src="{os.path.basename(plot_files[2])}" alt="Model Performance">
                <p class="visualization-caption">Figure 3: Sales volume by BMW model (Top performers highlighted in green)</p>
            </div>
            
            <h3>Top Performing Models</h3>
            {self._create_model_table(analysis_data['model_performance'])}
        </section>
        
        <section id="price-drivers">
            <h2>Price Drivers and Market Dynamics</h2>
            {self._format_text_with_paragraphs(llm_insights['drivers_analysis'])}
            
            <div class="visualization">
                <img src="{os.path.basename(plot_files[3])}" alt="Price Analysis">
                <p class="visualization-caption">Figure 4: Price distribution and relationship with sales volume</p>
            </div>
            
            <div class="visualization">
                <img src="{os.path.basename(plot_files[4])}" alt="Fuel Type Trends">
                <p class="visualization-caption">Figure 5: Fuel type preferences and trends over time</p>
            </div>
        </section>
"""
        
        # Add revenue section if available
        if len(plot_files) > 5 and os.path.exists(plot_files[5]):
            html_content += f"""
        <section id="revenue-analysis">
            <h2>Revenue Analysis</h2>
            <div class="visualization">
                <img src="{os.path.basename(plot_files[5])}" alt="Revenue Analysis">
                <p class="visualization-caption">Figure 6: Revenue breakdown by year, model, and region</p>
            </div>
        </section>
"""
        
        # Add correlation analysis
        if len(plot_files) > 6 and os.path.exists(plot_files[6]):
            html_content += f"""
        <section id="correlation-analysis">
            <h2>Correlation Analysis</h2>
            <div class="visualization">
                <img src="{os.path.basename(plot_files[6])}" alt="Correlation Heatmap">
                <p class="visualization-caption">Figure 7: Correlation heatmap of key performance metrics</p>
            </div>
        </section>
"""
        
        # Add model category if available
        if len(plot_files) > 7 and os.path.exists(plot_files[7]):
            html_content += f"""
        <section id="category-performance">
            <h2>Model Category Performance</h2>
            <div class="visualization">
                <img src="{os.path.basename(plot_files[7])}" alt="Model Category Performance">
                <p class="visualization-caption">Figure 8: Sales performance by model category</p>
            </div>
        </section>
"""
        
        html_content += f"""
        <section id="creative-insights">
            <h2>Creative Business Insights</h2>
            <div class="insight-box">
                {self._format_text_with_paragraphs(llm_insights['creative_insights'])}
            </div>
        </section>
        
        <section id="recommendations">
            <h2>Strategic Recommendations</h2>
            <div class="recommendation-box">
                {self._format_text_with_paragraphs(llm_insights['recommendations'])}
            </div>
        </section>
        
        <footer>
            <p><strong>BMW Sales Analysis System</strong></p>
            <p>Powered by Advanced Analytics and AI-Driven Insights</p>
            <p>Report generated automatically using OpenAI GPT-4 and Python</p>
        </footer>
    </div>
</body>
</html>
"""
        
        # Save HTML report
        html_path = os.path.join(self.output_dir, 'BMW_Sales_Analysis_Report.html')
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return html_path
    
    def generate_markdown_report(self,
                                 analysis_data: Dict[str, Any],
                                 llm_insights: Dict[str, str],
                                 plot_files: List[str]) -> str:
        """
        Generate Markdown report
        
        Parameters:
        -----------
        analysis_data : dict
            Statistical analysis data
        llm_insights : dict
            LLM-generated insights
        plot_files : list
            List of plot file paths
            
        Returns:
        --------
        str : Path to generated Markdown report
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        md_content = f"""# BMW Sales Analysis Report (2020-2024)

**Comprehensive Analysis of Sales Performance**  
*Generated on {timestamp}*

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Key Performance Metrics](#key-performance-metrics)
3. [Yearly Sales Trends](#yearly-sales-trends)
4. [Regional Performance Analysis](#regional-performance-analysis)
5. [Model Performance Analysis](#model-performance-analysis)
6. [Price Drivers and Market Dynamics](#price-drivers-and-market-dynamics)
7. [Creative Business Insights](#creative-business-insights)
8. [Strategic Recommendations](#strategic-recommendations)

---

## Executive Summary

{llm_insights['executive_summary']}

---

## Key Performance Metrics

| Metric | Value |
|--------|-------|
| **Total Sales Volume** | {analysis_data['overview']['total_sales_volume']:,} units |
| **Average Price** | ${analysis_data['overview']['avg_price']:,.2f} |
| **Total Models** | {analysis_data['overview']['total_models']} |
| **Global Regions** | {analysis_data['overview']['total_regions']} |
| **Years Covered** | {', '.join(map(str, analysis_data['overview']['years_covered']))} |

---

## Yearly Sales Trends

{llm_insights['yearly_analysis']}

![Yearly Sales Trends]({os.path.basename(plot_files[0])})  
*Figure 1: Sales volume and average price trends over time (2020-2024)*

### Yearly Performance Data

| Year | Total Sales | YoY Growth |
|------|------------|------------|
"""
        
        for year, sales in analysis_data['yearly_trends']['yearly_sales'].items():
            growth = analysis_data['yearly_trends']['yoy_growth_rate'].get(year, 0)
            md_content += f"| {year} | {sales:,} | {growth:.2f}% |\n"
        
        md_content += f"""
---

## Regional Performance Analysis

{llm_insights['regional_analysis']}

![Regional Performance]({os.path.basename(plot_files[1])})  
*Figure 2: Sales performance and market share by region*

### Regional Sales Breakdown

| Region | Sales Volume | Market Share |
|--------|--------------|--------------|
"""
        
        for region, sales in analysis_data['regional_performance']['regional_sales'].items():
            share = analysis_data['regional_performance']['regional_market_share'][region]
            md_content += f"| {region} | {sales:,} | {share:.2f}% |\n"
        
        md_content += f"""
---

## Model Performance Analysis

{llm_insights['model_analysis']}

![Model Performance]({os.path.basename(plot_files[2])})  
*Figure 3: Sales volume by BMW model (Top performers highlighted)*

### Top Performing Models

| Model | Sales Volume | Market Share | Avg Price |
|-------|--------------|--------------|-----------|
"""
        
        for model, sales in list(analysis_data['model_performance']['top_3_models'].items()):
            share = analysis_data['model_performance']['model_market_share'][model]
            price = analysis_data['model_performance']['avg_price_by_model'][model]
            md_content += f"| {model} | {sales:,} | {share:.2f}% | ${price:,.2f} |\n"
        
        md_content += f"""
---

## Price Drivers and Market Dynamics

{llm_insights['drivers_analysis']}

![Price Analysis]({os.path.basename(plot_files[3])})  
*Figure 4: Price distribution and relationship with sales volume*

![Fuel Type Trends]({os.path.basename(plot_files[4])})  
*Figure 5: Fuel type preferences and trends over time*

---
"""
        
        # Add revenue section if available
        if len(plot_files) > 5 and os.path.exists(plot_files[5]):
            md_content += f"""
## Revenue Analysis

![Revenue Analysis]({os.path.basename(plot_files[5])})  
*Figure 6: Revenue breakdown by year, model, and region*

---
"""
        
        # Add correlation analysis
        if len(plot_files) > 6 and os.path.exists(plot_files[6]):
            md_content += f"""
## Correlation Analysis

![Correlation Heatmap]({os.path.basename(plot_files[6])})  
*Figure 7: Correlation heatmap of key performance metrics*

---
"""
        
        md_content += f"""
## Creative Business Insights

{llm_insights['creative_insights']}

---

## Strategic Recommendations

{llm_insights['recommendations']}

---

## Report Information

**BMW Sales Analysis System**  
Powered by Advanced Analytics and AI-Driven Insights  
Report generated automatically using OpenAI GPT-4 and Python

---
"""
        
        # Save Markdown report
        md_path = os.path.join(self.output_dir, 'BMW_Sales_Analysis_Report.md')
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        return md_path
    
    def _format_text_with_paragraphs(self, text: str) -> str:
        """Format text into HTML paragraphs"""
        paragraphs = text.strip().split('\n\n')
        formatted = []
        
        for para in paragraphs:
            para = para.strip()
            if para:
                # Check if it's a list item or heading
                if para.startswith(('- ', '* ', '1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ')):
                    # It's a list, wrap in ul/ol
                    if para[0].isdigit():
                        formatted.append('<ol>')
                    else:
                        formatted.append('<ul>')
                    
                    for line in para.split('\n'):
                        if line.strip():
                            # Remove list markers
                            clean_line = line.strip()
                            for marker in ['- ', '* ', '1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ']:
                                if clean_line.startswith(marker):
                                    clean_line = clean_line[len(marker):]
                                    break
                            formatted.append(f'<li>{clean_line}</li>')
                    
                    if para[0].isdigit():
                        formatted.append('</ol>')
                    else:
                        formatted.append('</ul>')
                elif para.startswith('#'):
                    # It's a heading
                    level = para.count('#', 0, 4)
                    text = para.lstrip('#').strip()
                    formatted.append(f'<h{level+2}>{text}</h{level+2}>')
                else:
                    # Regular paragraph
                    formatted.append(f'<p>{para}</p>')
        
        return '\n'.join(formatted)
    
    def _create_regional_table(self, regional_data: Dict[str, Any]) -> str:
        """Create HTML table for regional performance"""
        html = '<table class="data-table"><thead><tr><th>Region</th><th>Sales Volume</th><th>Market Share</th><th>Avg Price</th></tr></thead><tbody>'
        
        for region, sales in regional_data['regional_sales'].items():
            share = regional_data['regional_market_share'][region]
            price = regional_data['avg_price_by_region'][region]
            html += f'<tr><td>{region}</td><td>{sales:,}</td><td>{share:.2f}%</td><td>${price:,.2f}</td></tr>'
        
        html += '</tbody></table>'
        return html
    
    def _create_model_table(self, model_data: Dict[str, Any]) -> str:
        """Create HTML table for model performance"""
        html = '<table class="data-table"><thead><tr><th>Model</th><th>Sales Volume</th><th>Market Share</th><th>Avg Price</th></tr></thead><tbody>'
        
        for model, sales in model_data['top_3_models'].items():
            share = model_data['model_market_share'][model]
            price = model_data['avg_price_by_model'][model]
            html += f'<tr><td><strong>{model}</strong></td><td>{sales:,}</td><td>{share:.2f}%</td><td>${price:,.2f}</td></tr>'
        
        html += '</tbody></table>'
        return html
