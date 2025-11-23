"""
Unit tests for report_evaluator module
"""

import unittest
import os
import json
import tempfile
import sys

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from report_evaluator import ReportEvaluator


class TestReportEvaluator(unittest.TestCase):
    """Test cases for ReportEvaluator class"""

    def setUp(self):
        """Set up test fixtures"""
        self.temp_dir = tempfile.mkdtemp()
        self.evaluator = ReportEvaluator(output_dir=self.temp_dir)

        # Sample analysis data
        self.analysis_data = {
            "overview": {
                "total_records": 1000,
                "years_covered": [2020, 2021, 2022, 2023, 2024],
                "total_years": 5,
                "total_models": 10,
                "total_regions": 3,
                "total_sales_volume": 50000,
                "avg_price": 60000,
            },
            "yearly_trends": {
                "yearly_sales": {
                    2020: 10000,
                    2021: 11000,
                    2022: 10500,
                    2023: 9000,
                    2024: 9500,
                }
            },
            "regional_performance": {
                "regional_sales": {
                    "North America": 20000,
                    "Europe": 18000,
                    "Asia": 12000,
                }
            },
            "model_performance": {
                "model_sales": {"X5": 15000, "3 Series": 12000, "X3": 10000}
            },
            "price_analysis": {"price_elasticity_indicator": -0.3},
            "correlation_analysis": {"correlation_matrix": {}},
        }

        # Sample LLM insights
        self.llm_insights = {
            "executive_summary": "This is a comprehensive executive summary with over 200 characters. "
            * 3,
            "yearly_analysis": "Detailed yearly analysis with specific metrics like 15% growth. "
            * 3,
            "regional_analysis": "Regional performance shows North America leading with 40% market share. "
            * 3,
            "model_analysis": "Model X5 dominates with 30% of total sales volume. " * 3,
            "drivers_analysis": "Price elasticity of -0.3 indicates moderate price sensitivity. "
            * 3,
            "creative_insights": "Unique patterns reveal opportunities in emerging markets. "
            * 3,
            "recommendations": "Strategic recommendations include expanding SUV lineup. "
            * 3,
        }

        # Create dummy HTML report
        self.html_path = os.path.join(self.temp_dir, "test_report.html")
        with open(self.html_path, "w", encoding="utf-8") as f:
            f.write("<html><head><title>BMW Report</title></head><body>")
            f.write("<h1>BMW Sales Analysis</h1>")
            f.write('<div class="section">Content</div>')
            f.write("</body></html>")

        # Create dummy Markdown report
        self.md_path = os.path.join(self.temp_dir, "test_report.md")
        with open(self.md_path, "w", encoding="utf-8") as f:
            f.write("# BMW Sales Analysis\n\n")
            f.write("## Section\n\nContent\n")

    def tearDown(self):
        """Clean up test fixtures"""
        import shutil

        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    def test_initialization(self):
        """Test evaluator initialization"""
        self.assertIsNotNone(self.evaluator)
        self.assertTrue(os.path.exists(self.evaluator.evaluation_dir))

    def test_evaluate_correctness(self):
        """Test correctness evaluation"""
        result = self.evaluator._evaluate_correctness(
            self.analysis_data, self.llm_insights
        )

        self.assertIn("score", result)
        self.assertIn("issues", result)
        self.assertIn("status", result)
        self.assertTrue(0 <= result["score"] <= 100)

    def test_evaluate_completeness(self):
        """Test completeness evaluation"""
        result = self.evaluator._evaluate_completeness(
            self.analysis_data, self.llm_insights
        )

        self.assertIn("score", result)
        self.assertIn("issues", result)
        self.assertIn("status", result)
        self.assertTrue(0 <= result["score"] <= 100)

    def test_evaluate_readability(self):
        """Test readability evaluation"""
        result = self.evaluator._evaluate_readability(self.html_path, self.md_path)

        self.assertIn("score", result)
        self.assertIn("issues", result)
        self.assertIn("status", result)
        self.assertTrue(0 <= result["score"] <= 100)

    def test_evaluate_data_quality(self):
        """Test data quality evaluation"""
        result = self.evaluator._evaluate_data_quality(self.analysis_data)

        self.assertIn("score", result)
        self.assertIn("issues", result)
        self.assertIn("status", result)
        self.assertTrue(0 <= result["score"] <= 100)

    def test_evaluate_insight_quality(self):
        """Test insight quality evaluation"""
        result = self.evaluator._evaluate_insight_quality(self.llm_insights)

        self.assertIn("score", result)
        self.assertIn("issues", result)
        self.assertIn("status", result)
        self.assertTrue(0 <= result["score"] <= 100)

    def test_get_grade(self):
        """Test grade calculation"""
        self.assertEqual(self.evaluator._get_grade(95), "A")
        self.assertEqual(self.evaluator._get_grade(85), "B")
        self.assertEqual(self.evaluator._get_grade(75), "C")
        self.assertEqual(self.evaluator._get_grade(65), "D")
        self.assertEqual(self.evaluator._get_grade(55), "F")

    def test_full_evaluation(self):
        """Test complete evaluation workflow"""
        evaluation = self.evaluator.evaluate_report(
            self.analysis_data, self.llm_insights, self.html_path, self.md_path
        )

        # Verify structure
        self.assertIn("timestamp", evaluation)
        self.assertIn("correctness", evaluation)
        self.assertIn("completeness", evaluation)
        self.assertIn("readability", evaluation)
        self.assertIn("data_quality", evaluation)
        self.assertIn("insight_quality", evaluation)
        self.assertIn("overall_score", evaluation)
        self.assertIn("grade", evaluation)

        # Verify score range
        self.assertTrue(0 <= evaluation["overall_score"] <= 100)

        # Verify evaluation file was created
        eval_files = [
            f for f in os.listdir(self.evaluator.evaluation_dir) if f.endswith(".json")
        ]
        self.assertGreater(len(eval_files), 0)

    def test_missing_html_file(self):
        """Test evaluation with missing HTML file"""
        result = self.evaluator._evaluate_readability("nonexistent.html", self.md_path)

        self.assertLess(result["score"], 100)
        self.assertTrue(any("HTML" in issue for issue in result["issues"]))

    def test_incomplete_insights(self):
        """Test evaluation with incomplete insights"""
        incomplete_insights = {"executive_summary": "Short summary"}

        result = self.evaluator._evaluate_completeness(
            self.analysis_data, incomplete_insights
        )

        self.assertLess(result["score"], 100)
        self.assertGreater(len(result["issues"]), 0)


if __name__ == "__main__":
    unittest.main()
