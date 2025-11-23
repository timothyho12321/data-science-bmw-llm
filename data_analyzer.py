"""
Data Analysis Module for BMW Sales Data
Performs statistical analysis and generates insights
"""

import pandas as pd
import numpy as np
from typing import Dict, Any


class BMWDataAnalyzer:
    """Analyzes BMW sales data and generates statistical insights"""

    def __init__(self, data_path: str):
        """
        Initialize the analyzer with cleaned data

        Parameters:
        -----------
        data_path : str
            Path to the cleaned Excel file
        """
        self.df = pd.read_excel(data_path)
        self.insights = {}

    def analyze_all(self) -> Dict[str, Any]:
        """
        Run all analysis methods and return comprehensive insights

        Returns:
        --------
        Dict containing all analysis results
        """
        self.insights = {
            "overview": self.get_overview(),
            "yearly_trends": self.analyze_yearly_trends(),
            "regional_performance": self.analyze_regional_performance(),
            "model_performance": self.analyze_model_performance(),
            "price_analysis": self.analyze_price_drivers(),
            "fuel_type_analysis": self.analyze_fuel_type_trends(),
            "transmission_analysis": self.analyze_transmission_preference(),
            "revenue_analysis": self.analyze_revenue(),
            "correlation_analysis": self.analyze_correlations(),
        }
        return self.insights

    def get_overview(self) -> Dict[str, Any]:
        """Get dataset overview statistics"""
        return {
            "total_records": len(self.df),
            "years_covered": sorted(self.df["Year"].unique().tolist()),
            "total_years": len(self.df["Year"].unique()),
            "total_models": self.df["Model"].nunique(),
            "total_regions": self.df["Region"].nunique(),
            "total_sales_volume": int(self.df["Sales_Volume"].sum()),
            "total_revenue": (
                float(self.df["Total_Revenue"].sum())
                if "Total_Revenue" in self.df.columns
                else None
            ),
            "avg_price": float(self.df["Price_USD"].mean()),
            "avg_sales_per_record": float(self.df["Sales_Volume"].mean()),
        }

    def analyze_yearly_trends(self) -> Dict[str, Any]:
        """Analyze sales trends by year"""
        yearly_stats = (
            self.df.groupby("Year")
            .agg(
                {
                    "Sales_Volume": ["sum", "mean"],
                    "Price_USD": "mean",
                    "Total_Revenue": (
                        "sum" if "Total_Revenue" in self.df.columns else "count"
                    ),
                }
            )
            .round(2)
        )

        yearly_sales = self.df.groupby("Year")["Sales_Volume"].sum()

        # Calculate year-over-year growth
        yoy_growth = yearly_sales.pct_change() * 100

        return {
            "yearly_sales": yearly_sales.to_dict(),
            "yearly_avg_price": self.df.groupby("Year")["Price_USD"].mean().to_dict(),
            "yoy_growth_rate": yoy_growth.dropna().to_dict(),
            "best_year": int(yearly_sales.idxmax()),
            "worst_year": int(yearly_sales.idxmin()),
            "total_growth": float(
                (
                    (yearly_sales.iloc[-1] - yearly_sales.iloc[0])
                    / yearly_sales.iloc[0]
                    * 100
                )
            ),
        }

    def analyze_regional_performance(self) -> Dict[str, Any]:
        """Analyze performance by region"""
        regional_stats = (
            self.df.groupby("Region")
            .agg(
                {
                    "Sales_Volume": "sum",
                    "Price_USD": "mean",
                    "Total_Revenue": (
                        "sum" if "Total_Revenue" in self.df.columns else "count"
                    ),
                }
            )
            .round(2)
        )

        regional_sales = (
            self.df.groupby("Region")["Sales_Volume"].sum().sort_values(ascending=False)
        )

        return {
            "regional_sales": regional_sales.to_dict(),
            "top_region": regional_sales.idxmax(),
            "bottom_region": regional_sales.idxmin(),
            "regional_market_share": (regional_sales / regional_sales.sum() * 100)
            .round(2)
            .to_dict(),
            "avg_price_by_region": self.df.groupby("Region")["Price_USD"]
            .mean()
            .sort_values(ascending=False)
            .to_dict(),
        }

    def analyze_model_performance(self) -> Dict[str, Any]:
        """Analyze performance by model"""
        model_sales = (
            self.df.groupby("Model")["Sales_Volume"].sum().sort_values(ascending=False)
        )
        model_revenue = (
            self.df.groupby("Model")["Total_Revenue"].sum().sort_values(ascending=False)
            if "Total_Revenue" in self.df.columns
            else None
        )

        # Model category analysis if available
        if "Model_Category" in self.df.columns:
            category_sales = (
                self.df.groupby("Model_Category")["Sales_Volume"]
                .sum()
                .sort_values(ascending=False)
            )
            category_data = category_sales.to_dict()
        else:
            category_data = None

        return {
            "model_sales": model_sales.to_dict(),
            "top_3_models": model_sales.head(3).to_dict(),
            "bottom_3_models": model_sales.tail(3).to_dict(),
            "model_market_share": (model_sales / model_sales.sum() * 100)
            .round(2)
            .to_dict(),
            "avg_price_by_model": self.df.groupby("Model")["Price_USD"]
            .mean()
            .sort_values(ascending=False)
            .to_dict(),
            "model_category_sales": category_data,
        }

    def analyze_price_drivers(self) -> Dict[str, Any]:
        """Analyze relationship between price and sales"""
        if "Price_Category" in self.df.columns:
            price_cat_sales = (
                self.df.groupby("Price_Category")["Sales_Volume"].sum().to_dict()
            )
        else:
            price_cat_sales = None

        # Bin prices for analysis
        price_bins = [0, 50000, 75000, 100000, float("inf")]
        price_labels = ["Budget", "Mid-Range", "Premium", "Luxury"]
        self.df["Price_Bin"] = pd.cut(
            self.df["Price_USD"], bins=price_bins, labels=price_labels
        )

        price_segment_sales = (
            self.df.groupby("Price_Bin")["Sales_Volume"].sum().to_dict()
        )

        return {
            "price_category_sales": price_cat_sales,
            "price_segment_sales": price_segment_sales,
            "avg_sales_by_price_segment": self.df.groupby("Price_Bin")["Sales_Volume"]
            .mean()
            .to_dict(),
            "price_elasticity_indicator": float(
                self.df["Price_USD"].corr(self.df["Sales_Volume"])
            ),
        }

    def analyze_fuel_type_trends(self) -> Dict[str, Any]:
        """Analyze fuel type preferences over time"""
        fuel_sales = (
            self.df.groupby("Fuel_Type")["Sales_Volume"]
            .sum()
            .sort_values(ascending=False)
        )

        # Yearly fuel type trends
        fuel_yearly = (
            self.df.groupby(["Year", "Fuel_Type"])["Sales_Volume"]
            .sum()
            .unstack(fill_value=0)
        )

        return {
            "fuel_type_sales": fuel_sales.to_dict(),
            "fuel_market_share": (fuel_sales / fuel_sales.sum() * 100)
            .round(2)
            .to_dict(),
            "fuel_yearly_trends": fuel_yearly.to_dict(),
            "most_popular_fuel": fuel_sales.idxmax(),
        }

    def analyze_transmission_preference(self) -> Dict[str, Any]:
        """Analyze transmission type preferences"""
        trans_sales = self.df.groupby("Transmission")["Sales_Volume"].sum()

        return {
            "transmission_sales": trans_sales.to_dict(),
            "transmission_market_share": (trans_sales / trans_sales.sum() * 100)
            .round(2)
            .to_dict(),
            "preferred_transmission": trans_sales.idxmax(),
        }

    def analyze_revenue(self) -> Dict[str, Any]:
        """Analyze revenue metrics"""
        if "Total_Revenue" not in self.df.columns:
            return None

        total_revenue = self.df["Total_Revenue"].sum()
        revenue_by_year = self.df.groupby("Year")["Total_Revenue"].sum()
        revenue_by_model = (
            self.df.groupby("Model")["Total_Revenue"].sum().sort_values(ascending=False)
        )
        revenue_by_region = (
            self.df.groupby("Region")["Total_Revenue"]
            .sum()
            .sort_values(ascending=False)
        )

        return {
            "total_revenue": float(total_revenue),
            "revenue_by_year": revenue_by_year.to_dict(),
            "top_revenue_models": revenue_by_model.head(5).to_dict(),
            "top_revenue_regions": revenue_by_region.head(3).to_dict(),
            "avg_revenue_per_sale": float(self.df["Total_Revenue"].mean()),
        }

    def analyze_correlations(self) -> Dict[str, Any]:
        """Analyze correlations between numerical variables"""
        numerical_cols = ["Price_USD", "Sales_Volume", "Engine_Size_L", "Mileage_KM"]
        if "Total_Revenue" in self.df.columns:
            numerical_cols.append("Total_Revenue")

        corr_matrix = self.df[numerical_cols].corr()

        # Find strongest correlations (excluding diagonal)
        corr_pairs = []
        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                corr_pairs.append(
                    {
                        "var1": corr_matrix.columns[i],
                        "var2": corr_matrix.columns[j],
                        "correlation": float(corr_matrix.iloc[i, j]),
                    }
                )

        corr_pairs.sort(key=lambda x: abs(x["correlation"]), reverse=True)

        return {
            "correlation_matrix": corr_matrix.to_dict(),
            "top_correlations": corr_pairs[:5],
        }

    def get_summary_for_llm(self) -> str:
        """
        Generate a formatted summary for LLM consumption

        Returns:
        --------
        Formatted string summary of all insights
        """
        if not self.insights:
            self.analyze_all()

        summary = f"""
BMW SALES DATA ANALYSIS SUMMARY (2020-2024)

=== OVERVIEW ===
- Total Records: {self.insights['overview']['total_records']:,}
- Years Covered: {', '.join(map(str, self.insights['overview']['years_covered']))}
- Total Models: {self.insights['overview']['total_models']}
- Total Regions: {self.insights['overview']['total_regions']}
- Total Sales Volume: {self.insights['overview']['total_sales_volume']:,} units
- Average Price: ${self.insights['overview']['avg_price']:,.2f}

=== YEARLY TRENDS ===
- Best Performing Year: {self.insights['yearly_trends']['best_year']}
- Worst Performing Year: {self.insights['yearly_trends']['worst_year']}
- Overall Growth (2020-2024): {self.insights['yearly_trends']['total_growth']:.2f}%
- Yearly Sales: {self.insights['yearly_trends']['yearly_sales']}

=== REGIONAL PERFORMANCE ===
- Top Region: {self.insights['regional_performance']['top_region']}
- Bottom Region: {self.insights['regional_performance']['bottom_region']}
- Regional Market Share: {self.insights['regional_performance']['regional_market_share']}

=== MODEL PERFORMANCE ===
- Top 3 Models: {list(self.insights['model_performance']['top_3_models'].keys())}
- Bottom 3 Models: {list(self.insights['model_performance']['bottom_3_models'].keys())}
- Model Sales Distribution: {self.insights['model_performance']['model_sales']}

=== PRICE ANALYSIS ===
- Price-Sales Correlation: {self.insights['price_analysis']['price_elasticity_indicator']:.3f}
- Sales by Price Segment: {self.insights['price_analysis']['price_segment_sales']}

=== FUEL TYPE TRENDS ===
- Most Popular Fuel Type: {self.insights['fuel_type_analysis']['most_popular_fuel']}
- Fuel Type Market Share: {self.insights['fuel_type_analysis']['fuel_market_share']}

=== TRANSMISSION PREFERENCE ===
- Preferred Transmission: {self.insights['transmission_analysis']['preferred_transmission']}
- Market Share: {self.insights['transmission_analysis']['transmission_market_share']}
"""

        if self.insights.get("revenue_analysis"):
            summary += f"""
=== REVENUE ANALYSIS ===
- Total Revenue: ${self.insights['revenue_analysis']['total_revenue']:,.2f}
- Top Revenue Models: {list(self.insights['revenue_analysis']['top_revenue_models'].keys())}
- Top Revenue Regions: {list(self.insights['revenue_analysis']['top_revenue_regions'].keys())}
"""

        return summary
