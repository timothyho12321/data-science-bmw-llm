.PHONY: help install install-dev test lint format clean docker-build docker-run docker-clean run

help:
	@echo "BMW Sales Analysis System - Available commands:"
	@echo "  make install       - Install production dependencies"
	@echo "  make install-dev   - Install development dependencies"
	@echo "  make test          - Run tests with coverage"
	@echo "  make lint          - Run linting checks"
	@echo "  make format        - Format code with black and isort"
	@echo "  make clean         - Clean up generated files"
	@echo "  make docker-build  - Build Docker image"
	@echo "  make docker-run    - Run analysis in Docker"
	@echo "  make docker-clean  - Clean Docker containers and images"
	@echo "  make run           - Run analysis locally"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

test:
	pytest tests/ -v --cov=. --cov-report=html --cov-report=term

lint:
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
	pylint *.py --disable=C0103,C0114,C0115,C0116

format:
	black .
	isort .

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	find . -type d -name '*.egg-info' -exec rm -rf {} +
	rm -rf build dist .pytest_cache .coverage htmlcov
	rm -f test_data.xlsx

docker-build:
	docker build -t bmw-sales-analysis:latest .

docker-run:
	docker-compose up bmw-analysis

docker-clean:
	docker-compose down
	docker rmi bmw-sales-analysis:latest

run:
	python analyze_bmw_sales.py

clean-data:
	python read_bmw_data.py
