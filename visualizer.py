"""
Visualization Module for BMW Sales Data
Generates professional charts and plots
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from typing import List, Dict, Any
import numpy as np

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10


class BMWDataVisualizer:
    """Creates visualizations for BMW sales data analysis"""
    
    def __init__(self, data_path: str, output_dir: str = "reports"):
        """
        Initialize the visualizer
        
        Parameters:
        -----------
        data_path : str
            Path to the cleaned Excel file
        output_dir : str
            Directory to save generated plots
        """
        self.df = pd.read_excel(data_path)
        self.output_dir = output_dir
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        self.generated_plots = []
    
    def generate_all_plots(self) -> List[str]:
        """
        Generate all visualization plots
        
        Returns:
        --------
        List of file paths to generated plots
        """
        self.generated_plots = []
        
        # Generate each plot type
        self.plot_yearly_sales_trend()
        self.plot_regional_performance()
        self.plot_model_performance()
        self.plot_price_distribution()
        self.plot_fuel_type_trends()
        self.plot_revenue_analysis()
        self.plot_correlation_heatmap()
        self.plot_model_category_performance()
        
        return self.generated_plots
    
    def plot_yearly_sales_trend(self):
        """Plot sales trends over years"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Total sales by year
        yearly_sales = self.df.groupby('Year')['Sales_Volume'].sum()
        ax1.plot(yearly_sales.index, yearly_sales.values, marker='o', linewidth=2, markersize=8, color='#1f77b4')
        ax1.set_title('Total Sales Volume by Year', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Year', fontsize=12)
        ax1.set_ylabel('Total Sales Volume', fontsize=12)
        ax1.grid(True, alpha=0.3)
        
        # Add value labels
        for x, y in zip(yearly_sales.index, yearly_sales.values):
            ax1.text(x, y, f'{int(y):,}', ha='center', va='bottom', fontsize=9)
        
        # Average price by year
        yearly_price = self.df.groupby('Year')['Price_USD'].mean()
        ax2.bar(yearly_price.index, yearly_price.values, color='#2ca02c', alpha=0.7)
        ax2.set_title('Average Price by Year', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Year', fontsize=12)
        ax2.set_ylabel('Average Price (USD)', fontsize=12)
        ax2.grid(True, alpha=0.3, axis='y')
        
        # Add value labels
        for x, y in zip(yearly_price.index, yearly_price.values):
            ax2.text(x, y, f'${int(y):,}', ha='center', va='bottom', fontsize=9)
        
        plt.tight_layout()
        filepath = os.path.join(self.output_dir, '01_yearly_sales_trend.png')
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        self.generated_plots.append(filepath)
    
    def plot_regional_performance(self):
        """Plot regional sales performance"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Sales by region
        regional_sales = self.df.groupby('Region')['Sales_Volume'].sum().sort_values(ascending=True)
        ax1.barh(regional_sales.index, regional_sales.values, color='#ff7f0e', alpha=0.7)
        ax1.set_title('Total Sales Volume by Region', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Total Sales Volume', fontsize=12)
        ax1.set_ylabel('Region', fontsize=12)
        ax1.grid(True, alpha=0.3, axis='x')
        
        # Add value labels
        for i, (region, value) in enumerate(regional_sales.items()):
            ax1.text(value, i, f' {int(value):,}', va='center', fontsize=9)
        
        # Market share pie chart
        market_share = self.df.groupby('Region')['Sales_Volume'].sum()
        colors = plt.cm.Set3(range(len(market_share)))
        ax2.pie(market_share.values, labels=market_share.index, autopct='%1.1f%%', 
                startangle=90, colors=colors)
        ax2.set_title('Regional Market Share', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        filepath = os.path.join(self.output_dir, '02_regional_performance.png')
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        self.generated_plots.append(filepath)
    
    def plot_model_performance(self):
        """Plot model performance comparison"""
        fig, ax = plt.subplots(figsize=(14, 8))
        
        # Sales by model
        model_sales = self.df.groupby('Model')['Sales_Volume'].sum().sort_values(ascending=True)
        bars = ax.barh(model_sales.index, model_sales.values, color='#d62728', alpha=0.7)
        
        # Color top 3 differently
        top_3_indices = list(range(len(model_sales)-3, len(model_sales)))
        for idx in top_3_indices:
            bars[idx].set_color('#2ca02c')
            bars[idx].set_alpha(0.8)
        
        ax.set_title('Sales Volume by Model (Top 3 in Green)', fontsize=14, fontweight='bold')
        ax.set_xlabel('Total Sales Volume', fontsize=12)
        ax.set_ylabel('Model', fontsize=12)
        ax.grid(True, alpha=0.3, axis='x')
        
        # Add value labels
        for i, (model, value) in enumerate(model_sales.items()):
            ax.text(value, i, f' {int(value):,}', va='center', fontsize=9)
        
        plt.tight_layout()
        filepath = os.path.join(self.output_dir, '03_model_performance.png')
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        self.generated_plots.append(filepath)
    
    def plot_price_distribution(self):
        """Plot price distribution and relationship with sales"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Price distribution histogram
        ax1.hist(self.df['Price_USD'], bins=30, color='#9467bd', alpha=0.7, edgecolor='black')
        ax1.set_title('Price Distribution', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Price (USD)', fontsize=12)
        ax1.set_ylabel('Frequency', fontsize=12)
        ax1.grid(True, alpha=0.3, axis='y')
        ax1.axvline(self.df['Price_USD'].mean(), color='red', linestyle='--', linewidth=2, label='Mean')
        ax1.axvline(self.df['Price_USD'].median(), color='green', linestyle='--', linewidth=2, label='Median')
        ax1.legend()
        
        # Price vs Sales scatter plot
        # Aggregate by price bins to avoid overplotting
        price_bins = pd.cut(self.df['Price_USD'], bins=20)
        price_sales_agg = self.df.groupby(price_bins).agg({
            'Price_USD': 'mean',
            'Sales_Volume': 'sum'
        })
        
        ax2.scatter(price_sales_agg['Price_USD'], price_sales_agg['Sales_Volume'], 
                   alpha=0.6, s=100, color='#8c564b')
        ax2.set_title('Price vs Total Sales Volume', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Average Price (USD)', fontsize=12)
        ax2.set_ylabel('Total Sales Volume', fontsize=12)
        ax2.grid(True, alpha=0.3)
        
        # Add trend line
        z = np.polyfit(price_sales_agg['Price_USD'], price_sales_agg['Sales_Volume'], 1)
        p = np.poly1d(z)
        ax2.plot(price_sales_agg['Price_USD'], p(price_sales_agg['Price_USD']), 
                "r--", alpha=0.8, linewidth=2, label='Trend')
        ax2.legend()
        
        plt.tight_layout()
        filepath = os.path.join(self.output_dir, '04_price_analysis.png')
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        self.generated_plots.append(filepath)
    
    def plot_fuel_type_trends(self):
        """Plot fuel type trends over time"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Fuel type sales over years
        fuel_yearly = self.df.groupby(['Year', 'Fuel_Type'])['Sales_Volume'].sum().unstack(fill_value=0)
        fuel_yearly.plot(kind='line', ax=ax1, marker='o', linewidth=2)
        ax1.set_title('Fuel Type Sales Trends Over Time', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Year', fontsize=12)
        ax1.set_ylabel('Sales Volume', fontsize=12)
        ax1.legend(title='Fuel Type', loc='best')
        ax1.grid(True, alpha=0.3)
        
        # Total fuel type distribution
        fuel_total = self.df.groupby('Fuel_Type')['Sales_Volume'].sum().sort_values(ascending=True)
        ax2.barh(fuel_total.index, fuel_total.values, color=['#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])
        ax2.set_title('Total Sales by Fuel Type', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Total Sales Volume', fontsize=12)
        ax2.set_ylabel('Fuel Type', fontsize=12)
        ax2.grid(True, alpha=0.3, axis='x')
        
        # Add value labels
        for i, (fuel, value) in enumerate(fuel_total.items()):
            ax2.text(value, i, f' {int(value):,}', va='center', fontsize=9)
        
        plt.tight_layout()
        filepath = os.path.join(self.output_dir, '05_fuel_type_trends.png')
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        self.generated_plots.append(filepath)
    
    def plot_revenue_analysis(self):
        """Plot revenue analysis if revenue data exists"""
        if 'Total_Revenue' not in self.df.columns:
            return
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        
        # Revenue by year
        yearly_revenue = self.df.groupby('Year')['Total_Revenue'].sum() / 1e9  # Convert to billions
        ax1.bar(yearly_revenue.index, yearly_revenue.values, color='#1f77b4', alpha=0.7)
        ax1.set_title('Total Revenue by Year', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Year', fontsize=12)
        ax1.set_ylabel('Revenue (Billion USD)', fontsize=12)
        ax1.grid(True, alpha=0.3, axis='y')
        
        for x, y in zip(yearly_revenue.index, yearly_revenue.values):
            ax1.text(x, y, f'${y:.2f}B', ha='center', va='bottom', fontsize=9)
        
        # Revenue by model (top 8)
        model_revenue = self.df.groupby('Model')['Total_Revenue'].sum().sort_values(ascending=False).head(8) / 1e6
        ax2.barh(range(len(model_revenue)), model_revenue.values, color='#2ca02c', alpha=0.7)
        ax2.set_yticks(range(len(model_revenue)))
        ax2.set_yticklabels(model_revenue.index)
        ax2.set_title('Top 8 Models by Revenue', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Revenue (Million USD)', fontsize=12)
        ax2.grid(True, alpha=0.3, axis='x')
        
        for i, value in enumerate(model_revenue.values):
            ax2.text(value, i, f' ${value:.1f}M', va='center', fontsize=9)
        
        # Revenue by region
        region_revenue = self.df.groupby('Region')['Total_Revenue'].sum().sort_values(ascending=False) / 1e9
        ax3.bar(range(len(region_revenue)), region_revenue.values, color='#ff7f0e', alpha=0.7)
        ax3.set_xticks(range(len(region_revenue)))
        ax3.set_xticklabels(region_revenue.index, rotation=45, ha='right')
        ax3.set_title('Revenue by Region', fontsize=14, fontweight='bold')
        ax3.set_ylabel('Revenue (Billion USD)', fontsize=12)
        ax3.grid(True, alpha=0.3, axis='y')
        
        for i, value in enumerate(region_revenue.values):
            ax3.text(i, value, f'${value:.2f}B', ha='center', va='bottom', fontsize=9)
        
        # Sales Volume vs Revenue scatter
        model_metrics = self.df.groupby('Model').agg({
            'Sales_Volume': 'sum',
            'Total_Revenue': 'sum'
        })
        ax4.scatter(model_metrics['Sales_Volume'], model_metrics['Total_Revenue'] / 1e6, 
                   s=100, alpha=0.6, color='#d62728')
        ax4.set_title('Sales Volume vs Revenue by Model', fontsize=14, fontweight='bold')
        ax4.set_xlabel('Total Sales Volume', fontsize=12)
        ax4.set_ylabel('Revenue (Million USD)', fontsize=12)
        ax4.grid(True, alpha=0.3)
        
        # Annotate points
        for model, row in model_metrics.iterrows():
            ax4.annotate(model, (row['Sales_Volume'], row['Total_Revenue'] / 1e6),
                        fontsize=8, alpha=0.7)
        
        plt.tight_layout()
        filepath = os.path.join(self.output_dir, '06_revenue_analysis.png')
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        self.generated_plots.append(filepath)
    
    def plot_correlation_heatmap(self):
        """Plot correlation heatmap for numerical variables"""
        numerical_cols = ['Price_USD', 'Sales_Volume', 'Engine_Size_L', 'Mileage_KM']
        if 'Total_Revenue' in self.df.columns:
            numerical_cols.append('Total_Revenue')
        
        # Calculate correlation matrix
        corr_matrix = self.df[numerical_cols].corr()
        
        # Create heatmap
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, fmt='.3f', cmap='coolwarm', 
                   center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8}, ax=ax)
        ax.set_title('Correlation Heatmap of Key Metrics', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        filepath = os.path.join(self.output_dir, '07_correlation_heatmap.png')
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        self.generated_plots.append(filepath)
    
    def plot_model_category_performance(self):
        """Plot model category performance if available"""
        if 'Model_Category' not in self.df.columns:
            return
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Sales by category
        category_sales = self.df.groupby('Model_Category')['Sales_Volume'].sum().sort_values(ascending=True)
        ax1.barh(category_sales.index, category_sales.values, color='#e377c2', alpha=0.7)
        ax1.set_title('Sales Volume by Model Category', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Total Sales Volume', fontsize=12)
        ax1.set_ylabel('Model Category', fontsize=12)
        ax1.grid(True, alpha=0.3, axis='x')
        
        for i, (cat, value) in enumerate(category_sales.items()):
            ax1.text(value, i, f' {int(value):,}', va='center', fontsize=9)
        
        # Category trends over years
        category_yearly = self.df.groupby(['Year', 'Model_Category'])['Sales_Volume'].sum().unstack(fill_value=0)
        category_yearly.plot(kind='bar', ax=ax2, width=0.8)
        ax2.set_title('Model Category Sales Trends', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Year', fontsize=12)
        ax2.set_ylabel('Sales Volume', fontsize=12)
        ax2.legend(title='Model Category', loc='best')
        ax2.grid(True, alpha=0.3, axis='y')
        ax2.set_xticklabels(ax2.get_xticklabels(), rotation=0)
        
        plt.tight_layout()
        filepath = os.path.join(self.output_dir, '08_model_category_performance.png')
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        self.generated_plots.append(filepath)
