"""
BMW Sales Analysis - Main Orchestration Script
Coordinates the entire LLM-powered analysis and reporting workflow
"""

import os
import sys
from datetime import datetime
from data_analyzer import BMWDataAnalyzer
from visualizer import BMWDataVisualizer
from report_generator import ReportGenerator

# Import LLM module based on ROLE environment variable
role = os.getenv('ROLE', 'Business Analyst').strip()
if role.lower() in ['business chief', 'executive', 'chief']:
    from llm_insights_executive import LLMInsightGenerator
    print(f"🎯 Analysis Mode: Executive Level ({role})")
else:
    from llm_insights import LLMInsightGenerator
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
    if not os.path.exists('.env'):
        print("❌ Error: .env file not found")
        print()
        print("Please create a .env file with your OpenAI API key:")
        print("  1. Copy .env.example to .env")
        print("  2. Add your OpenAI API key: OPENAI_API_KEY=your_key_here")
        print()
        return False
    return True


def main():
    """Main execution function"""
    print_banner()
    
    # Configuration
    data_path = os.path.join("data-bmw", "BMW sales data (2020-2024) Cleaned.xlsx")
    output_dir = "reports"
    
    # Step 1: Validate prerequisites
    print("Step 1: Validating prerequisites...")
    print("-" * 80)
    
    if not check_data_file(data_path):
        sys.exit(1)
    print(f"✓ Found cleaned data file: {data_path}")
    
    if not check_env_file():
        sys.exit(1)
    print("✓ Found .env file with API configuration")
    print()
    
    # Step 2: Data Analysis
    print("Step 2: Performing statistical analysis...")
    print("-" * 80)
    try:
        analyzer = BMWDataAnalyzer(data_path)
        analysis_data = analyzer.analyze_all()
        print(f"✓ Analysis complete!")
        print(f"  - Analyzed {analysis_data['overview']['total_records']:,} records")
        print(f"  - Covering {analysis_data['overview']['total_years']} years ({', '.join(map(str, analysis_data['overview']['years_covered']))})")
        print(f"  - {analysis_data['overview']['total_models']} models across {analysis_data['overview']['total_regions']} regions")
        print()
    except Exception as e:
        print(f"❌ Error during analysis: {str(e)}")
        sys.exit(1)
    
    # Step 3: Generate Visualizations
    print("Step 3: Generating visualizations...")
    print("-" * 80)
    try:
        visualizer = BMWDataVisualizer(data_path, output_dir)
        plot_files = visualizer.generate_all_plots()
        print(f"✓ Generated {len(plot_files)} visualizations")
        for plot in plot_files:
            print(f"  - {os.path.basename(plot)}")
        print()
    except Exception as e:
        print(f"❌ Error generating visualizations: {str(e)}")
        sys.exit(1)
    
    # Step 4: Generate LLM Insights
    print("Step 4: Generating LLM-powered insights...")
    print("-" * 80)
    try:
        llm_generator = LLMInsightGenerator()
        print("")
        llm_insights = llm_generator.generate_all_insights(analysis_data)
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
        print(f"❌ Error: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error generating LLM insights: {str(e)}")
        print("Please check your OpenAI API key and internet connection.")
        sys.exit(1)
    
    # Step 5: Generate Reports
    print("Step 5: Generating final reports...")
    print("-" * 80)
    try:
        report_gen = ReportGenerator(output_dir)
        
        # Generate HTML report
        html_path = report_gen.generate_html_report(analysis_data, llm_insights, plot_files)
        print(f"✓ Generated HTML report: {html_path}")
        
        # Generate Markdown report
        md_path = report_gen.generate_markdown_report(analysis_data, llm_insights, plot_files)
        print(f"✓ Generated Markdown report: {md_path}")
        print()
    except Exception as e:
        print(f"❌ Error generating reports: {str(e)}")
        sys.exit(1)
    
    # Summary
    print("=" * 80)
    print("✓ ANALYSIS COMPLETE!")
    print("=" * 80)
    print()
    print("Generated Files:")
    print(f"  📊 HTML Report: {html_path}")
    print(f"  📝 Markdown Report: {md_path}")
    print(f"  📈 Visualizations: {len(plot_files)} charts in '{output_dir}/' directory")
    print()
    print(f"Total execution time: {datetime.now().strftime('%H:%M:%S')}")
    print()
    print("To view the report, open the HTML file in your web browser:")
    print(f"  {os.path.abspath(html_path)}")
    print()
    print("=" * 80)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Analysis interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
