"""
Unit tests for data_analyzer module
"""

import unittest
import pandas as pd
import numpy as np
from unittest.mock import Mock, patch
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data_analyzer import BMWDataAnalyzer


class TestBMWDataAnalyzer(unittest.TestCase):
    """Test cases for BMWDataAnalyzer class"""

    @classmethod
    def setUpClass(cls):
        """Set up test fixtures"""
        # Create sample test data
        cls.test_data = pd.DataFrame(
            {
                "Model": ["X5", "3 Series", "X3", "X5", "3 Series"] * 20,
                "Year": [2020, 2021, 2022, 2023, 2024] * 20,
                "Region": ["North America", "Europe", "Asia", "North America", "Europe"]
                * 20,
                "Color": ["Black", "White", "Blue", "Red", "Silver"] * 20,
                "Fuel_Type": ["Petrol", "Diesel", "Electric", "Hybrid", "Petrol"] * 20,
                "Transmission": [
                    "Automatic",
                    "Automatic",
                    "Automatic",
                    "Manual",
                    "Automatic",
                ]
                * 20,
                "Engine_Size_L": [3.0, 2.0, 2.5, 3.0, 2.0] * 20,
                "Mileage_KM": [50000, 30000, 40000, 60000, 25000] * 20,
                "Price_USD": [75000, 45000, 60000, 80000, 50000] * 20,
                "Sales_Volume": [100, 150, 120, 90, 140] * 20,
                "Total_Revenue": [7500000, 6750000, 7200000, 7200000, 7000000] * 20,
                "Price_Category": [
                    "Premium",
                    "Budget",
                    "Mid-Range",
                    "Premium",
                    "Mid-Range",
                ]
                * 20,
                "Model_Category": ["SUV", "Sedan", "SUV", "SUV", "Sedan"] * 20,
            }
        )

        # Save to temporary file
        cls.test_file = "test_data.xlsx"
        cls.test_data.to_excel(cls.test_file, index=False)

    @classmethod
    def tearDownClass(cls):
        """Clean up test fixtures"""
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)

    def setUp(self):
        """Set up each test"""
        self.analyzer = BMWDataAnalyzer(self.test_file)

    def test_initialization(self):
        """Test analyzer initialization"""
        self.assertIsNotNone(self.analyzer.df)
        self.assertEqual(len(self.analyzer.df), 100)
        self.assertEqual(len(self.analyzer.df.columns), 13)

    def test_get_overview(self):
        """Test overview statistics generation"""
        overview = self.analyzer.get_overview()

        self.assertIn("total_records", overview)
        self.assertIn("years_covered", overview)
        self.assertIn("total_years", overview)
        self.assertIn("total_models", overview)
        self.assertIn("total_regions", overview)
        self.assertIn("total_sales_volume", overview)

        self.assertEqual(overview["total_records"], 100)
        self.assertEqual(overview["total_years"], 5)
        self.assertGreater(overview["total_sales_volume"], 0)

    def test_analyze_yearly_trends(self):
        """Test yearly trends analysis"""
        trends = self.analyzer.analyze_yearly_trends()

        self.assertIn("yearly_sales", trends)
        self.assertIn("yearly_avg_price", trends)
        self.assertIn("yoy_growth_rate", trends)
        self.assertIn("best_year", trends)
        self.assertIn("worst_year", trends)

        # Verify data types
        self.assertIsInstance(trends["yearly_sales"], dict)
        self.assertIsInstance(trends["best_year"], (int, np.integer))

    def test_analyze_regional_performance(self):
        """Test regional performance analysis"""
        regional = self.analyzer.analyze_regional_performance()

        self.assertIn("regional_sales", regional)
        self.assertIn("top_region", regional)
        self.assertIn("bottom_region", regional)
        self.assertIn("regional_market_share", regional)

        # Verify market share sums to ~100%
        total_share = sum(regional["regional_market_share"].values())
        self.assertAlmostEqual(total_share, 100.0, places=1)

    def test_analyze_model_performance(self):
        """Test model performance analysis"""
        models = self.analyzer.analyze_model_performance()

        self.assertIn("model_sales", models)
        self.assertIn("top_3_models", models)
        self.assertIn("bottom_3_models", models)
        self.assertIn("model_market_share", models)

        # Verify top 3 models
        self.assertEqual(len(models["top_3_models"]), 3)

    def test_analyze_price_drivers(self):
        """Test price driver analysis"""
        price = self.analyzer.analyze_price_drivers()

        self.assertIn("price_category_sales", price)
        self.assertIn("price_elasticity_indicator", price)

        # Verify elasticity is a valid correlation coefficient
        self.assertTrue(-1 <= price["price_elasticity_indicator"] <= 1)

    def test_analyze_fuel_type_trends(self):
        """Test fuel type trends analysis"""
        fuel = self.analyzer.analyze_fuel_type_trends()

        self.assertIn("fuel_type_sales", fuel)
        self.assertIn("fuel_market_share", fuel)
        self.assertIn("most_popular_fuel", fuel)

        # Verify market share sums to ~100%
        total_share = sum(fuel["fuel_market_share"].values())
        self.assertAlmostEqual(total_share, 100.0, places=1)

    def test_analyze_correlations(self):
        """Test correlation analysis"""
        corr = self.analyzer.analyze_correlations()

        self.assertIn("correlation_matrix", corr)
        self.assertIn("strongest_correlations", corr)

        # Verify correlation matrix structure
        self.assertIsInstance(corr["correlation_matrix"], dict)

    def test_analyze_all(self):
        """Test comprehensive analysis"""
        insights = self.analyzer.analyze_all()

        # Verify all expected sections
        expected_sections = [
            "overview",
            "yearly_trends",
            "regional_performance",
            "model_performance",
            "price_analysis",
            "fuel_type_analysis",
            "transmission_analysis",
            "revenue_analysis",
            "correlation_analysis",
        ]

        for section in expected_sections:
            self.assertIn(section, insights)

    def test_invalid_file_path(self):
        """Test handling of invalid file path"""
        with self.assertRaises(FileNotFoundError):
            BMWDataAnalyzer("nonexistent_file.xlsx")


if __name__ == "__main__":
    unittest.main()
