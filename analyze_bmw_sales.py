"""
BMW Sales Analysis - Main Orchestration Script
Coordinates the entire LLM-powered analysis and reporting workflow

Production-grade features:
- Comprehensive logging
- Error handling and recovery
- Report quality evaluation
- Modular design with clear separation of concerns
"""

import os
import sys
from datetime import datetime
from data_analyzer import BMWDataAnalyzer
from visualizer import BMWDataVisualizer
from report_generator import ReportGenerator
from report_evaluator import ReportEvaluator
from logger_config import LoggerSetup

# Initialize logger
logger = LoggerSetup.get_logger(__name__)

# Import LLM module based on ROLE environment variable
role = os.getenv("ROLE", "Business Analyst").strip()
if role.lower() in ["business chief", "executive", "chief"]:
    from llm_insights_executive import LLMInsightGenerator

    logger.info(f"Analysis Mode: Executive Level ({role})")
    print(f"🎯 Analysis Mode: Executive Level ({role})")
else:
    from llm_insights import LLMInsightGenerator

    logger.info(f"Analysis Mode: Business Analyst Level ({role})")
    print(f"📊 Analysis Mode: Business Analyst Level ({role})")


def print_banner():
    """Print welcome banner"""
    print("=" * 80)
    print("BMW SALES ANALYSIS SYSTEM")
    print("LLM-Powered Business Intelligence and Reporting")
    print("=" * 80)
    print()


def check_data_file(data_path: str) -> bool:
    """Check if the cleaned data file exists"""
    if not os.path.exists(data_path):
        print(f"❌ Error: Cleaned data file not found at: {data_path}")
        print()
        print("Please run 'python read_bmw_data.py' first to clean the data.")
        return False
    return True


def check_env_file() -> bool:
    """Check if .env file exists"""
    logger.debug("Checking for .env file")
    if not os.path.exists(".env"):
        logger.error(".env file not found")
        print("❌ Error: .env file not found")
        print()
        print("Please create a .env file with your LLM API key:")
        print("  1. Copy .env.example to .env")
        print("  2. Configure your preferred LLM provider (OpenAI or Gemini)")
        print()
        return False
    logger.debug(".env file found")
    return True


def validate_environment() -> bool:
    """
    Validate that all required environment variables are set

    Returns:
    --------
    bool : True if environment is valid
    """
    logger.info("Validating environment configuration")

    from dotenv import load_dotenv

    load_dotenv()

    provider = os.getenv("LLM_PROVIDER", "openai").lower()
    logger.info(f"LLM Provider: {provider}")

    if provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or api_key.startswith("your_"):
            logger.error("Invalid OpenAI API key")
            print("❌ Error: Please set a valid OPENAI_API_KEY in .env file")
            return False
    elif provider == "gemini":
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key or api_key.startswith("your_"):
            logger.error("Invalid Gemini API key")
            print("❌ Error: Please set a valid GEMINI_API_KEY in .env file")
            return False
    else:
        logger.error(f"Unsupported LLM provider: {provider}")
        print(f"❌ Error: Unsupported LLM_PROVIDER: {provider}")
        return False

    logger.info("Environment validation passed")
    return True


def main():
    """Main execution function with comprehensive error handling and logging"""
    start_time = datetime.now()
    logger.info("=" * 80)
    logger.info("BMW SALES ANALYSIS SYSTEM - STARTING")
    logger.info("=" * 80)

    print_banner()

    # Configuration
    data_path = os.path.join("data-bmw", "BMW sales data (2020-2024) Cleaned.xlsx")
    output_dir = "reports"

    # Step 1: Validate prerequisites
    print("Step 1: Validating prerequisites...")
    print("-" * 80)
    logger.info("Step 1: Validating prerequisites")

    if not check_data_file(data_path):
        logger.error("Data file validation failed")
        sys.exit(1)
    print(f"✓ Found cleaned data file: {data_path}")

    if not check_env_file():
        logger.error("Environment file validation failed")
        sys.exit(1)

    if not validate_environment():
        logger.error("Environment configuration validation failed")
        sys.exit(1)

    print("✓ Found .env file with API configuration")
    print()

    # Step 2: Data Analysis
    print("Step 2: Performing statistical analysis...")
    print("-" * 80)
    logger.info("Step 2: Starting statistical analysis")
    try:
        analyzer = BMWDataAnalyzer(data_path)
        analysis_data = analyzer.analyze_all()
        logger.info(
            f"Analysis complete - {analysis_data['overview']['total_records']} records analyzed"
        )
        print(f"✓ Analysis complete!")
        print(f"  - Analyzed {analysis_data['overview']['total_records']:,} records")
        print(
            f"  - Covering {analysis_data['overview']['total_years']} years ({', '.join(map(str, analysis_data['overview']['years_covered']))})"
        )
        print(
            f"  - {analysis_data['overview']['total_models']} models across {analysis_data['overview']['total_regions']} regions"
        )
        print()
    except Exception as e:
        logger.error(f"Error during analysis: {str(e)}", exc_info=True)
        print(f"❌ Error during analysis: {str(e)}")
        sys.exit(1)

    # Step 3: Generate Visualizations
    print("Step 3: Generating visualizations...")
    print("-" * 80)
    logger.info("Step 3: Starting visualization generation")
    try:
        visualizer = BMWDataVisualizer(data_path, output_dir)
        plot_files = visualizer.generate_all_plots()
        logger.info(f"Generated {len(plot_files)} visualizations")
        print(f"✓ Generated {len(plot_files)} visualizations")
        for plot in plot_files:
            print(f"  - {os.path.basename(plot)}")
        print()
    except Exception as e:
        logger.error(f"Error generating visualizations: {str(e)}", exc_info=True)
        print(f"❌ Error generating visualizations: {str(e)}")
        sys.exit(1)

    # Step 4: Generate LLM Insights
    print("Step 4: Generating LLM-powered insights...")
    print("-" * 80)
    logger.info("Step 4: Starting LLM insight generation")
    try:
        llm_generator = LLMInsightGenerator()
        print("")
        llm_insights = llm_generator.generate_all_insights(analysis_data)
        logger.info("LLM insights generated successfully")
        print("✓ Generated comprehensive insights:")
        print("  - Executive Summary")
        print("  - Yearly Trends Analysis")
        print("  - Regional Performance Analysis")
        print("  - Model Performance Analysis")
        print("  - Price Drivers Analysis")
        print("  - Creative Business Insights")
        print("  - Strategic Recommendations")
        print()
    except ValueError as e:
        logger.error(f"Configuration error: {str(e)}", exc_info=True)
        print(f"❌ Error: {str(e)}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error generating LLM insights: {str(e)}", exc_info=True)
        print(f"❌ Error generating LLM insights: {str(e)}")
        print("Please check your API key and internet connection.")
        sys.exit(1)

    # Step 5: Generate Reports
    print("Step 5: Generating final reports...")
    print("-" * 80)
    logger.info("Step 5: Starting report generation")
    try:
        report_gen = ReportGenerator(output_dir)

        # Generate HTML report
        html_path = report_gen.generate_html_report(
            analysis_data, llm_insights, plot_files
        )
        logger.info(f"HTML report generated: {html_path}")
        print(f"✓ Generated HTML report: {html_path}")

        # Generate Markdown report
        md_path = report_gen.generate_markdown_report(
            analysis_data, llm_insights, plot_files
        )
        logger.info(f"Markdown report generated: {md_path}")
        print(f"✓ Generated Markdown report: {md_path}")
        print()
    except Exception as e:
        logger.error(f"Error generating reports: {str(e)}", exc_info=True)
        print(f"❌ Error generating reports: {str(e)}")
        sys.exit(1)

    # Step 6: Evaluate Report Quality
    print("Step 6: Evaluating report quality...")
    print("-" * 80)
    logger.info("Step 6: Starting report quality evaluation")
    try:
        evaluator = ReportEvaluator(output_dir)
        evaluation = evaluator.evaluate_report(
            analysis_data, llm_insights, html_path, md_path
        )

        # Display evaluation summary
        print(f"✓ Report evaluation complete!")
        print(f"  - Overall Score: {evaluation['overall_score']:.1f}/100")
        print(f"  - Grade: {evaluation['grade']}")
        print(
            f"  - Correctness: {evaluation['correctness']['score']:.1f}/100 [{evaluation['correctness']['status']}]"
        )
        print(
            f"  - Completeness: {evaluation['completeness']['score']:.1f}/100 [{evaluation['completeness']['status']}]"
        )
        print(
            f"  - Readability: {evaluation['readability']['score']:.1f}/100 [{evaluation['readability']['status']}]"
        )

        # Generate and save evaluation report
        eval_report = evaluator.generate_evaluation_report(evaluation)
        eval_report_path = os.path.join(
            output_dir,
            "evaluations",
            f"evaluation_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
        )
        with open(eval_report_path, "w", encoding="utf-8") as f:
            f.write(eval_report)
        logger.info(f"Evaluation report saved: {eval_report_path}")
        print(f"  - Detailed evaluation: {eval_report_path}")
        print()

    except Exception as e:
        logger.warning(
            f"Error during evaluation (non-critical): {str(e)}", exc_info=True
        )
        print(
            f"⚠ Warning: Report evaluation encountered issues but analysis completed successfully"
        )
        print()

    # Summary
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()

    print("=" * 80)
    print("✓ ANALYSIS COMPLETE!")
    print("=" * 80)
    print()
    print("Generated Files:")
    print(f"  📊 HTML Report: {html_path}")
    print(f"  📝 Markdown Report: {md_path}")
    print(f"  📈 Visualizations: {len(plot_files)} charts in '{output_dir}/' directory")
    print(f"  📋 Evaluation: {eval_report_path}")
    print()
    print(f"Total execution time: {duration:.2f} seconds")
    print()
    
    # Detect if running in Docker and provide appropriate instructions
    is_docker = os.path.exists('/.dockerenv') or os.getenv('DOCKER_CONTAINER') == 'true'
    
    if is_docker:
        print("To view the report, open this file in your Windows browser:")
        print(f"  The report is available at: ./reports/BMW_Sales_Analysis_Report.html")
        print(f"  (Mapped from Docker volume to your host machine)")
    else:
        print("To view the report, open the HTML file in your web browser:")
        print(f"  {os.path.abspath(html_path)}")
    print()
    print("=" * 80)

    logger.info(f"Analysis completed successfully in {duration:.2f} seconds")
    logger.info("=" * 80)


if __name__ == "__main__":
    try:
        logger.info("Application started")
        main()
        logger.info("Application completed successfully")
    except KeyboardInterrupt:
        logger.warning("Analysis interrupted by user")
        print("\n\n⚠️ Analysis interrupted by user.")
        sys.exit(0)
    except Exception as e:
        logger.critical(f"Unexpected error: {str(e)}", exc_info=True)
        print(f"\n\n❌ Unexpected error: {str(e)}")
        import traceback

        traceback.print_exc()
        sys.exit(1)
