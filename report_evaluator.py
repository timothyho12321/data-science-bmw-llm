"""
Report Quality Evaluation Framework
Assesses the quality of generated reports based on multiple criteria
"""

import os
import json
from typing import Dict, Any, List, Tuple
from datetime import datetime
from logger_config import LoggerSetup

logger = LoggerSetup.get_logger(__name__)


class ReportEvaluator:
    """Evaluates report quality across multiple dimensions"""

    def __init__(self, output_dir: str = "reports"):
        """
        Initialize report evaluator

        Parameters:
        -----------
        output_dir : str
            Directory containing reports to evaluate
        """
        self.output_dir = output_dir
        self.evaluation_dir = os.path.join(output_dir, "evaluations")
        os.makedirs(self.evaluation_dir, exist_ok=True)
        logger.info(f"Initialized ReportEvaluator with output_dir: {output_dir}")

    def evaluate_report(
        self,
        analysis_data: Dict[str, Any],
        llm_insights: Dict[str, str],
        html_path: str,
        md_path: str,
    ) -> Dict[str, Any]:
        """
        Comprehensive report quality evaluation

        Parameters:
        -----------
        analysis_data : dict
            Statistical analysis data
        llm_insights : dict
            LLM-generated insights
        html_path : str
            Path to HTML report
        md_path : str
            Path to Markdown report

        Returns:
        --------
        dict : Evaluation results with scores and feedback
        """
        logger.info("Starting comprehensive report evaluation")

        evaluation = {
            "timestamp": datetime.now().isoformat(),
            "correctness": self._evaluate_correctness(analysis_data, llm_insights),
            "completeness": self._evaluate_completeness(analysis_data, llm_insights),
            "readability": self._evaluate_readability(html_path, md_path),
            "data_quality": self._evaluate_data_quality(analysis_data),
            "insight_quality": self._evaluate_insight_quality(llm_insights),
        }

        # Calculate overall score
        scores = [
            evaluation["correctness"]["score"],
            evaluation["completeness"]["score"],
            evaluation["readability"]["score"],
            evaluation["data_quality"]["score"],
            evaluation["insight_quality"]["score"],
        ]
        evaluation["overall_score"] = sum(scores) / len(scores)
        evaluation["grade"] = self._get_grade(evaluation["overall_score"])

        # Save evaluation
        self._save_evaluation(evaluation)

        logger.info(
            f"Evaluation complete. Overall score: {evaluation['overall_score']:.2f}/100 ({evaluation['grade']})"
        )
        return evaluation

    def _evaluate_correctness(
        self, analysis_data: Dict[str, Any], llm_insights: Dict[str, str]
    ) -> Dict[str, Any]:
        """
        Evaluate correctness of data and insights

        Criteria:
        - Data consistency
        - Mathematical accuracy
        - Logical coherence
        """
        logger.debug("Evaluating correctness")

        issues = []
        score = 100

        # Check for required analysis sections
        required_sections = [
            "overview",
            "yearly_trends",
            "regional_performance",
            "model_performance",
            "price_analysis",
        ]
        missing_sections = [s for s in required_sections if s not in analysis_data]
        if missing_sections:
            score -= len(missing_sections) * 10
            issues.append(f"Missing analysis sections: {', '.join(missing_sections)}")

        # Verify data consistency
        if "overview" in analysis_data:
            total_records = analysis_data["overview"].get("total_records", 0)
            if total_records == 0:
                score -= 20
                issues.append("No records found in dataset")
            elif total_records < 100:
                score -= 10
                issues.append(f"Low record count: {total_records}")

        # Check for negative values where inappropriate
        if "price_analysis" in analysis_data:
            avg_price = analysis_data["price_analysis"].get("avg_price", 0)
            if avg_price < 0:
                score -= 15
                issues.append("Negative average price detected")

        # Verify LLM insights are present and substantial
        for key, insight in llm_insights.items():
            if not insight or len(insight) < 50:
                score -= 5
                issues.append(
                    f"Insufficient insight for {key}: only {len(insight)} characters"
                )

        return {
            "score": max(0, score),
            "issues": issues,
            "status": "PASS" if score >= 70 else "FAIL",
        }

    def _evaluate_completeness(
        self, analysis_data: Dict[str, Any], llm_insights: Dict[str, str]
    ) -> Dict[str, Any]:
        """
        Evaluate completeness of report coverage

        Criteria:
        - All required sections present
        - Comprehensive data coverage
        - Complete insights
        """
        logger.debug("Evaluating completeness")

        score = 100
        issues = []

        # Expected LLM insight sections
        expected_insights = [
            "executive_summary",
            "yearly_analysis",
            "regional_analysis",
            "model_analysis",
            "drivers_analysis",
            "creative_insights",
            "recommendations",
        ]

        missing_insights = [s for s in expected_insights if s not in llm_insights]
        if missing_insights:
            score -= len(missing_insights) * 10
            issues.append(f"Missing insight sections: {', '.join(missing_insights)}")

        # Check visualization coverage
        if "overview" in analysis_data:
            models_count = analysis_data["overview"].get("total_models", 0)
            regions_count = analysis_data["overview"].get("total_regions", 0)
            years_count = analysis_data["overview"].get("total_years", 0)

            if models_count < 5:
                score -= 5
                issues.append(f"Limited model coverage: {models_count} models")
            if regions_count < 3:
                score -= 5
                issues.append(f"Limited regional coverage: {regions_count} regions")
            if years_count < 3:
                score -= 5
                issues.append(f"Limited temporal coverage: {years_count} years")

        # Check for correlation analysis
        if "correlation_analysis" not in analysis_data:
            score -= 10
            issues.append("Missing correlation analysis")

        return {
            "score": max(0, score),
            "issues": issues,
            "status": "PASS" if score >= 70 else "FAIL",
        }

    def _evaluate_readability(self, html_path: str, md_path: str) -> Dict[str, Any]:
        """
        Evaluate readability of generated reports

        Criteria:
        - File accessibility
        - Proper formatting
        - Reasonable length
        """
        logger.debug("Evaluating readability")

        score = 100
        issues = []

        # Check HTML report
        if not os.path.exists(html_path):
            score -= 30
            issues.append("HTML report file not found")
        else:
            html_size = os.path.getsize(html_path)
            if html_size < 5000:
                score -= 15
                issues.append(f"HTML report too short: {html_size} bytes")
            elif html_size > 5000000:  # 5MB
                score -= 10
                issues.append(f"HTML report very large: {html_size} bytes")

            # Check HTML content
            try:
                with open(html_path, "r", encoding="utf-8") as f:
                    html_content = f.read()
                    if "<html" not in html_content.lower():
                        score -= 10
                        issues.append("Invalid HTML structure")
                    if "Executive Summary" not in html_content:
                        score -= 5
                        issues.append("Missing key sections in HTML")
            except Exception as e:
                score -= 10
                issues.append(f"Error reading HTML: {str(e)}")

        # Check Markdown report
        if not os.path.exists(md_path):
            score -= 20
            issues.append("Markdown report file not found")
        else:
            md_size = os.path.getsize(md_path)
            if md_size < 2000:
                score -= 10
                issues.append(f"Markdown report too short: {md_size} bytes")

        return {
            "score": max(0, score),
            "issues": issues,
            "status": "PASS" if score >= 70 else "FAIL",
        }

    def _evaluate_data_quality(self, analysis_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Evaluate quality of underlying data and analysis

        Criteria:
        - Data distribution
        - Statistical validity
        - Outlier handling
        """
        logger.debug("Evaluating data quality")

        score = 100
        issues = []

        if "overview" in analysis_data:
            overview = analysis_data["overview"]

            # Check data volume
            total_records = overview.get("total_records", 0)
            if total_records < 1000:
                score -= 15
                issues.append(f"Small dataset: {total_records} records")

            # Check temporal coverage
            years = overview.get("years_covered", [])
            if len(years) < 2:
                score -= 10
                issues.append("Insufficient temporal coverage")

        # Check for balanced data
        if "regional_performance" in analysis_data:
            regional = analysis_data["regional_performance"]
            sales_values = [
                v.get("total_sales", 0)
                for v in regional.values()
                if isinstance(v, dict)
            ]
            if sales_values:
                max_sales = max(sales_values)
                min_sales = min(sales_values)
                if max_sales > 0 and min_sales / max_sales < 0.1:
                    score -= 5
                    issues.append("Highly imbalanced regional distribution")

        return {
            "score": max(0, score),
            "issues": issues,
            "status": "PASS" if score >= 70 else "FAIL",
        }

    def _evaluate_insight_quality(self, llm_insights: Dict[str, str]) -> Dict[str, Any]:
        """
        Evaluate quality of LLM-generated insights

        Criteria:
        - Length adequacy
        - Specificity (numbers, percentages)
        - Actionability
        """
        logger.debug("Evaluating insight quality")

        score = 100
        issues = []

        for key, insight in llm_insights.items():
            if not insight:
                score -= 10
                issues.append(f"Empty insight: {key}")
                continue

            # Check length
            if len(insight) < 200:
                score -= 5
                issues.append(f"Short insight for {key}: {len(insight)} chars")

            # Check for specific numbers
            has_numbers = any(char.isdigit() for char in insight)
            if not has_numbers:
                score -= 3
                issues.append(f"No specific numbers in {key}")

            # Check for percentage symbols
            has_percentages = "%" in insight
            if not has_percentages and key not in ["creative_insights"]:
                score -= 2
                issues.append(f"No percentages in {key}")

        return {
            "score": max(0, score),
            "issues": issues,
            "status": "PASS" if score >= 70 else "FAIL",
        }

    def _get_grade(self, score: float) -> str:
        """Convert numeric score to letter grade"""
        if score >= 90:
            return "A (Excellent)"
        elif score >= 80:
            return "B (Good)"
        elif score >= 70:
            return "C (Satisfactory)"
        elif score >= 60:
            return "D (Needs Improvement)"
        else:
            return "F (Poor)"

    def _save_evaluation(self, evaluation: Dict[str, Any]):
        """Save evaluation results to JSON file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        eval_file = os.path.join(self.evaluation_dir, f"evaluation_{timestamp}.json")

        try:
            with open(eval_file, "w", encoding="utf-8") as f:
                json.dump(evaluation, f, indent=2)
            logger.info(f"Evaluation saved to: {eval_file}")
        except Exception as e:
            logger.error(f"Failed to save evaluation: {str(e)}")

    def generate_evaluation_report(self, evaluation: Dict[str, Any]) -> str:
        """
        Generate human-readable evaluation report

        Parameters:
        -----------
        evaluation : dict
            Evaluation results

        Returns:
        --------
        str : Formatted evaluation report
        """
        logger.info("Generating evaluation report")

        report = []
        report.append("=" * 80)
        report.append("BMW SALES ANALYSIS - REPORT QUALITY EVALUATION")
        report.append("=" * 80)
        report.append(f"Timestamp: {evaluation['timestamp']}")
        report.append(f"\nOVERALL SCORE: {evaluation['overall_score']:.1f}/100")
        report.append(f"GRADE: {evaluation['grade']}")
        report.append("\n" + "=" * 80)

        # Detailed scores
        report.append("\nDETAILED SCORES:")
        report.append("-" * 80)

        categories = [
            ("Correctness", "correctness"),
            ("Completeness", "completeness"),
            ("Readability", "readability"),
            ("Data Quality", "data_quality"),
            ("Insight Quality", "insight_quality"),
        ]

        for name, key in categories:
            cat_eval = evaluation[key]
            score = cat_eval["score"]
            status = cat_eval["status"]
            report.append(f"\n{name}: {score:.1f}/100 [{status}]")

            if cat_eval["issues"]:
                report.append("  Issues:")
                for issue in cat_eval["issues"]:
                    report.append(f"    - {issue}")

        report.append("\n" + "=" * 80)

        # Recommendations
        report.append("\nRECOMMENDATIONS:")
        report.append("-" * 80)

        if evaluation["overall_score"] >= 90:
            report.append("✓ Excellent report quality! Meets all production standards.")
        elif evaluation["overall_score"] >= 80:
            report.append("✓ Good report quality with minor issues to address.")
        elif evaluation["overall_score"] >= 70:
            report.append("⚠ Satisfactory quality but improvements needed.")
        else:
            report.append(
                "✗ Report quality below acceptable standards. Significant improvements required."
            )

        report.append("=" * 80)

        return "\n".join(report)
