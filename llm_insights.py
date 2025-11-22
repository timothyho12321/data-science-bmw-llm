"""
LLM Integration Module for BMW Sales Analysis
Uses OpenAI API to generate insights and narratives
"""

import os
from openai import OpenAI
from dotenv import load_dotenv
from typing import Dict, Any, List
import json

# Load environment variables
load_dotenv()


class LLMInsightGenerator:
    """Generates insights and narratives using OpenAI LLM"""
    
    def __init__(self):
        """Initialize OpenAI client"""
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables. Please create a .env file with your API key.")
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = os.getenv('OPENAI_MODEL', 'gpt-4')
        self.temperature = float(os.getenv('OPENAI_TEMPERATURE', '0.7'))
    
    def generate_executive_summary(self, analysis_data: Dict[str, Any]) -> str:
        """
        Generate executive summary from analysis data
        
        Parameters:
        -----------
        analysis_data : dict
            Dictionary containing all analysis insights
            
        Returns:
        --------
        str : Executive summary text
        """
        prompt = f"""
You are a senior business analyst for BMW. Based on the following sales data analysis from 2020-2024, 
write a concise executive summary (3-4 paragraphs) highlighting the most critical findings and their 
business implications.

ANALYSIS DATA:
{json.dumps(analysis_data, indent=2)}

Your executive summary should:
1. Start with the most impactful overall finding
2. Highlight 2-3 key performance metrics
3. Mention the most significant trend or pattern
4. Be written for C-level executives (clear, concise, actionable)
5. Use specific numbers from the data

Write in a professional, confident tone. Focus on insights, not just facts.
"""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert business analyst specializing in automotive sales data."},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
            max_tokens=800
        )
        
        return response.choices[0].message.content.strip()
    
    def analyze_yearly_trends(self, analysis_data: Dict[str, Any]) -> str:
        """
        Generate detailed analysis of yearly trends
        
        Parameters:
        -----------
        analysis_data : dict
            Dictionary containing yearly trends data
            
        Returns:
        --------
        str : Yearly trends analysis
        """
        prompt = f"""
You are analyzing BMW sales performance over time (2020-2024). Based on the following data, 
provide a detailed analysis of yearly trends:

YEARLY TRENDS DATA:
{json.dumps(analysis_data['yearly_trends'], indent=2)}

OVERVIEW DATA:
{json.dumps(analysis_data['overview'], indent=2)}

Your analysis should:
1. Identify and explain the sales performance trend over the 5-year period
2. Discuss year-over-year growth rates and what they indicate
3. Identify any inflection points or significant changes
4. Explain potential external factors that may have influenced these trends (e.g., market conditions, COVID-19 impact)
5. Discuss price trends and their relationship to sales volume
6. Provide forward-looking insights based on the trend

Be analytical and insightful. Use specific numbers and percentages. Write 4-5 paragraphs.
"""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert automotive industry analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
            max_tokens=1000
        )
        
        return response.choices[0].message.content.strip()
    
    def analyze_regional_performance(self, analysis_data: Dict[str, Any]) -> str:
        """
        Generate analysis of regional market performance
        
        Parameters:
        -----------
        analysis_data : dict
            Dictionary containing regional performance data
            
        Returns:
        --------
        str : Regional analysis
        """
        prompt = f"""
You are analyzing BMW's regional market performance. Based on the following data, 
provide a comprehensive analysis of regional sales:

REGIONAL DATA:
{json.dumps(analysis_data['regional_performance'], indent=2)}

Your analysis should:
1. Identify top-performing and underperforming regions with specific metrics
2. Explain the market share distribution and what it reveals
3. Discuss regional pricing strategies and their effectiveness
4. Identify opportunities for market expansion or improvement
5. Provide strategic recommendations for underperforming regions
6. Highlight any surprising or noteworthy regional patterns

Be specific with numbers and percentages. Write 4-5 paragraphs with actionable insights.
"""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert in global automotive market analysis."},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
            max_tokens=1000
        )
        
        return response.choices[0].message.content.strip()
    
    def analyze_model_performance(self, analysis_data: Dict[str, Any]) -> str:
        """
        Generate analysis of model/product performance
        
        Parameters:
        -----------
        analysis_data : dict
            Dictionary containing model performance data
            
        Returns:
        --------
        str : Model analysis
        """
        prompt = f"""
You are analyzing BMW's product portfolio performance. Based on the following data, 
provide a detailed analysis of model sales performance:

MODEL PERFORMANCE DATA:
{json.dumps(analysis_data['model_performance'], indent=2)}

Your analysis should:
1. Identify top-performing models and explain their success factors
2. Analyze underperforming models and potential reasons
3. Discuss the product mix and its impact on overall performance
4. Compare pricing strategies across different models
5. Identify portfolio gaps or opportunities
6. If model categories are available, analyze category performance (SUV, Sedan, Electric/Hybrid, Performance)

Provide strategic insights about product portfolio management. Write 4-5 paragraphs.
"""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert automotive product strategist."},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
            max_tokens=1000
        )
        
        return response.choices[0].message.content.strip()
    
    def analyze_price_drivers(self, analysis_data: Dict[str, Any]) -> str:
        """
        Analyze key drivers of sales including price
        
        Parameters:
        -----------
        analysis_data : dict
            Dictionary containing price and correlation analysis
            
        Returns:
        --------
        str : Price and drivers analysis
        """
        prompt = f"""
You are analyzing the key drivers of BMW sales. Based on the following data, 
provide insights into how price and other factors drive sales performance:

PRICE ANALYSIS:
{json.dumps(analysis_data['price_analysis'], indent=2)}

CORRELATION ANALYSIS:
{json.dumps(analysis_data['correlation_analysis'], indent=2)}

FUEL TYPE DATA:
{json.dumps(analysis_data['fuel_type_analysis'], indent=2)}

Your analysis should:
1. Analyze the relationship between price and sales volume (price elasticity)
2. Discuss performance across different price segments
3. Identify the strongest correlations and what they mean for business strategy
4. Analyze fuel type preferences and trends (electric vs traditional)
5. Discuss transmission preferences and market implications
6. Provide insights on optimal pricing strategies

Be analytical and data-driven. Write 4-5 paragraphs with strategic recommendations.
"""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert in pricing strategy and market analysis."},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
            max_tokens=1000
        )
        
        return response.choices[0].message.content.strip()
    
    def generate_creative_insights(self, analysis_data: Dict[str, Any]) -> str:
        """
        Generate 1-2 creative insights demonstrating business understanding
        
        Parameters:
        -----------
        analysis_data : dict
            Complete analysis data
            
        Returns:
        --------
        str : Creative insights
        """
        prompt = f"""
You are a strategic business consultant for BMW. Based on all the sales data analysis below, 
generate 1-2 creative and unexpected insights that demonstrate deep business understanding.

COMPLETE ANALYSIS DATA:
{json.dumps(analysis_data, indent=2)}

Your insights should:
1. Go beyond obvious findings to reveal hidden patterns or opportunities
2. Connect multiple data points in unexpected ways
3. Provide actionable strategic value
4. Demonstrate creativity and business acumen
5. Be surprising yet supported by the data

Examples of creative insights might include:
- Cross-market opportunities (e.g., success factors from one region applied to another)
- Product portfolio optimization strategies
- Emerging market trends or shifts
- Customer segment insights
- Competitive positioning opportunities

Provide 2 distinct, creative insights. Write 3-4 paragraphs total.
"""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a creative strategic business consultant with deep automotive industry expertise."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,  # Higher temperature for more creative output
            max_tokens=1000
        )
        
        return response.choices[0].message.content.strip()
    
    def generate_recommendations(self, analysis_data: Dict[str, Any]) -> str:
        """
        Generate strategic recommendations based on all insights
        
        Parameters:
        -----------
        analysis_data : dict
            Complete analysis data
            
        Returns:
        --------
        str : Strategic recommendations
        """
        prompt = f"""
You are the Chief Strategy Officer of BMW. Based on the comprehensive sales analysis below, 
provide 5-7 strategic recommendations for the business.

COMPLETE ANALYSIS:
{json.dumps(analysis_data, indent=2)}

Your recommendations should:
1. Be specific, actionable, and prioritized
2. Address both opportunities and challenges
3. Cover different aspects: product, pricing, markets, trends
4. Be data-driven with specific references to findings
5. Include both short-term tactics and long-term strategy
6. Be realistic and implementable

Format as a numbered list with each recommendation being 2-3 sentences explaining the what, why, and expected impact.
"""
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a senior executive providing strategic direction."},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
            max_tokens=1200
        )
        
        return response.choices[0].message.content.strip()
    
    def generate_all_insights(self, analysis_data: Dict[str, Any]) -> Dict[str, str]:
        """
        Generate all LLM-powered insights
        
        Parameters:
        -----------
        analysis_data : dict
            Complete analysis data from BMWDataAnalyzer
            
        Returns:
        --------
        Dict containing all generated insights
        """
        print("Generating LLM insights...")
        
        insights = {}
        
        print("  - Generating executive summary...")
        insights['executive_summary'] = self.generate_executive_summary(analysis_data)
        
        print("  - Analyzing yearly trends...")
        insights['yearly_analysis'] = self.analyze_yearly_trends(analysis_data)
        
        print("  - Analyzing regional performance...")
        insights['regional_analysis'] = self.analyze_regional_performance(analysis_data)
        
        print("  - Analyzing model performance...")
        insights['model_analysis'] = self.analyze_model_performance(analysis_data)
        
        print("  - Analyzing price drivers...")
        insights['drivers_analysis'] = self.analyze_price_drivers(analysis_data)
        
        print("  - Generating creative insights...")
        insights['creative_insights'] = self.generate_creative_insights(analysis_data)
        
        print("  - Generating recommendations...")
        insights['recommendations'] = self.generate_recommendations(analysis_data)
        
        print("✓ LLM insights generation complete!")
        
        return insights
