"""
LLM Integration Module for Executive-Level BMW Sales Analysis
Uses OpenAI API to generate high-level strategic insights
"""

import os
from openai import OpenAI
from dotenv import load_dotenv
from typing import Dict, Any, List
import json

# Load environment variables
load_dotenv()

class LLMInsightGenerator:
    """Generates high-level strategic insights using OpenAI LLM"""
    
    def __init__(self):
        """Initialize OpenAI client"""
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found. Please check your .env file.")
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = os.getenv('OPENAI_MODEL', 'gpt-4')
        self.temperature = float(os.getenv('OPENAI_TEMPERATURE', '0.7'))
        
        print(f"Using OpenAI model: {self.model}")
        if 'gpt-3.5' in self.model.lower():
            print("  → Using GPT-3.5-turbo (faster, more cost-effective)")
        elif 'gpt-4' in self.model.lower():
            print("  → Using GPT-4 (higher quality, more detailed insights)")

    def _get_system_prompt(self, role_description: str) -> str:
        """Helper to create consistent system prompts with formatting rules"""
        return f"""
        {role_description}
        
        CRITICAL OUTPUT RULES:
        1. Use professional Markdown formatting (## Headers, **Bold** for metrics).
        2. NEVER make vague statements (e.g., "sales went up"). ALWAYS cite the exact number or percentage from the data.
        3. Be concise and direct. Avoid fluff words like "Interestingly" or "It is worth noting."
        4. Focus on the "So What?" -> Why does this data point matter for the business?
        """

    def generate_executive_summary(self, analysis_data: Dict[str, Any]) -> str:
        prompt = f"""
        You are the Chief of Staff at BMW presenting to the Board of Directors. 
        Synthesize the provided sales data (2020-2024) into a high-impact Executive Summary.

        ANALYSIS DATA:
        {json.dumps(analysis_data, indent=2)}

        REQUIRED STRUCTURE:
        1. **The Bottom Line (BLUF):** One sentence summarizing the overall health of sales.
        2. **Critical KPIs:** A bulleted list of the 3 most important metrics (Total Volume, Revenue, or Growth %).
        3. **Primary Driver:** What single factor (region or model) contributed most to the success or failure?
        4. **Strategic Implication:** One sentence on what this data suggests for the next fiscal year.

        Keep it under 250 words. Punchy and authoritative.
        """
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self._get_system_prompt("You are a C-level Executive assistant.")},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
            max_tokens=800
        )
        return response.choices[0].message.content.strip()

    def analyze_yearly_trends(self, analysis_data: Dict[str, Any]) -> str:
        prompt = f"""
        Perform a Time-Series Analysis on the BMW sales data (2020-2024).

        YEARLY DATA:
        {json.dumps(analysis_data.get('yearly_trends', {}), indent=2)}
        OVERVIEW:
        {json.dumps(analysis_data.get('overview', {}), indent=2)}

        YOUR TASKS:
        1. **Calculate & Discuss Volatility:** Was growth linear, or were there sharp spikes/drops? Correlate drops with known global events if the years align (e.g., 2020-2021 Supply Chain/COVID).
        2. **Year-Over-Year (YoY) Velocity:** Don't just list totals. Highlight which year had the *fastest* acceleration or deceleration.
        3. **Revenue vs. Volume:** If data permits, analyze if revenue grew faster than volume (indicating price increases) or vice versa.

        Format as 3 distinct paragraphs using professional financial terminology.
        """
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self._get_system_prompt("You are a Financial Planning & Analysis (FP&A) Manager.")},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
            max_tokens=1000
        )
        return response.choices[0].message.content.strip()

    def analyze_regional_performance(self, analysis_data: Dict[str, Any]) -> str:
        prompt = f"""
        Analyze the geographic distribution of sales using the Pareto Principle (80/20 Rule).

        REGIONAL DATA:
        {json.dumps(analysis_data.get('regional_performance', {}), indent=2)}

        YOUR TASKS:
        1. **Identify the Powerhouses:** Which regions generate the majority of the volume? (e.g., "The top 2 regions account for X% of sales").
        2. **Growth vs. Stagnation:** Contrast a high-growth emerging market against a saturated mature market.
        3. **Risk Assessment:** Are we over-reliant on a single region?
        
        Provide a strategic recommendation for the underperforming regions: Exit, Invest, or Pivot?
        """
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self._get_system_prompt("You are a Global Market Strategist.")},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
            max_tokens=1000
        )
        return response.choices[0].message.content.strip()

    def analyze_model_performance(self, analysis_data: Dict[str, Any]) -> str:
        prompt = f"""
        Conduct a Product Portfolio Analysis (BCG Matrix style).

        MODEL DATA:
        {json.dumps(analysis_data.get('model_performance', {}), indent=2)}

        YOUR TASKS:
        1. **Identify the 'Cash Cows':** Which models provide steady, high volume?
        2. **Identify the 'Stars':** Which models are showing rapid growth?
        3. **Identify the 'Dogs':** Which models are dragging down performance?
        4. **Segment Shift:** Analyze the shift between traditional Sedans vs. SUVs/SAVs.
        
        Be specific: "The X5 outperforms the 3-series by Y%..."
        """
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self._get_system_prompt("You are a Product Portfolio Manager.")},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
            max_tokens=1000
        )
        return response.choices[0].message.content.strip()

    def analyze_price_drivers(self, analysis_data: Dict[str, Any]) -> str:
        prompt = f"""
        Analyze the Price Elasticity and Key Sales Drivers.

        PRICE & CORRELATION DATA:
        {json.dumps(analysis_data.get('price_analysis', {}), indent=2)}
        {json.dumps(analysis_data.get('correlation_analysis', {}), indent=2)}
        {json.dumps(analysis_data.get('fuel_type_analysis', {}), indent=2)}

        YOUR TASKS:
        1. **Price Sensitivity:** Does higher price strictly correlate with lower volume, or does the BMW brand command inelastic demand?
        2. **The EV Transition:** Specifically analyze the uptake of Electric/Hybrid fuel types compared to Petrol/Diesel. Is the growth rate sufficient to meet industry trends?
        3. **Transmission Trends:** Brief comment on Automatic vs. Manual trends if data exists.

        Focus on the economics of the sales.
        """
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self._get_system_prompt("You are a Pricing Economist.")},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
            max_tokens=1000
        )
        return response.choices[0].message.content.strip()

    def generate_creative_insights(self, analysis_data: Dict[str, Any]) -> str:
        prompt = f"""
        Ignore standard reporting. Look for "Second-Order Effects" and hidden anomalies in the data.

        COMPLETE DATA:
        {json.dumps(analysis_data, indent=2)}

        TASK:
        Generate 2 "Contrarian Insights." These should be non-obvious observations that a standard dashboard would miss.
        
        *Example of a contrarian insight:* "While Region A has the highest volume, its growth is flatlining, suggesting market saturation, whereas Region B has low volume but 200% growth."

        Give me 2 distinct, narrative paragraphs titled **Insight #1** and **Insight #2**.
        """
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self._get_system_prompt("You are a Data Detective looking for anomalies.")},
                {"role": "user", "content": prompt}
            ],
            temperature=0.85,  # Higher temp for creativity
            max_tokens=1000
        )
        return response.choices[0].message.content.strip()

    def generate_recommendations(self, analysis_data: Dict[str, Any]) -> str:
        prompt = f"""
        Based on all previous analysis, construct a 3-Point Strategic Action Plan.

        COMPLETE DATA:
        {json.dumps(analysis_data, indent=2)}

        The plan must be:
        - **Actionable:** Use verbs (e.g., "Divest," "Accelerate," "Bundle").
        - **Justified:** Reference the specific data point that triggers this recommendation.
        - **Prioritized:** Start with the highest ROI activity.

        Format as a bulleted list (use - not numbers).
        """
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self._get_system_prompt("You are a Strategy Consultant (McKinsey/BCG style).")},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
            max_tokens=1200
        )
        return response.choices[0].message.content.strip()

    def generate_all_insights(self, analysis_data: Dict[str, Any]) -> Dict[str, str]:
        """Orchestrates the generation of all insights"""
        print("Generating LLM insights (Executive Level)...")
        
        insights = {}
        # Execute sequentially (could be parallelized for speed, but sequential allows easier debugging)
        stages = [
            ('executive_summary', self.generate_executive_summary),
            ('yearly_analysis', self.analyze_yearly_trends),
            ('regional_analysis', self.analyze_regional_performance),
            ('model_analysis', self.analyze_model_performance),
            ('drivers_analysis', self.analyze_price_drivers),
            ('creative_insights', self.generate_creative_insights),
            ('recommendations', self.generate_recommendations)
        ]

        for key, func in stages:
            print(f"  - Generating {key.replace('_', ' ')}...")
            try:
                insights[key] = func(analysis_data)
            except Exception as e:
                print(f"    ! Error generating {key}: {e}")
                insights[key] = "Insight generation failed."

        print("✓ LLM insights generation complete!")
        return insights
