"""
Setup configuration for BMW Sales Analysis System
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [
        line.strip() for line in fh if line.strip() and not line.startswith("#")
    ]

setup(
    name="bmw-sales-analysis",
    version="1.0.0",
    author="Timothy Ho",
    author_email="timothyho12321@users.noreply.github.com",
    description="LLM-powered BMW sales data analysis and reporting system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/timothyho12321/data-science-bmw-llm",
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.12",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.7.0",
            "flake8>=6.1.0",
            "mypy>=1.5.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "bmw-analysis=analyze_bmw_sales:main",
            "bmw-clean-data=read_bmw_data:main",
        ],
    },
)
