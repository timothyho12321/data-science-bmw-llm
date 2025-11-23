# BMW Sales Analysis System - Docker Container
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libhdf5-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY *.py ./
COPY logger_config.py ./
COPY report_evaluator.py ./
COPY llm_provider.py ./
COPY llm_insights.py ./
COPY llm_insights_executive.py ./
COPY data_analyzer.py ./
COPY visualizer.py ./
COPY report_generator.py ./
COPY read_bmw_data.py ./

# Create directories for data and outputs
RUN mkdir -p /app/data-bmw /app/reports /app/logs

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Default command
CMD ["python", "analyze_bmw_sales.py"]
