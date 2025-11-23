# Testing Guide

## Overview

This document describes the testing strategy and procedures for the BMW Sales Analysis System.

## Test Structure

```
tests/
├── __init__.py
├── test_data_analyzer.py      # Unit tests for data analysis
├── test_llm_provider.py        # Unit tests for LLM provider
└── test_report_evaluator.py   # Unit tests for report evaluation
```

## Running Tests

### Run All Tests
```bash
pytest
```

### Run Tests with Coverage
```bash
pytest --cov=. --cov-report=html --cov-report=term-missing
```

### Run Specific Test File
```bash
pytest tests/test_data_analyzer.py -v
```

### Run Specific Test
```bash
pytest tests/test_data_analyzer.py::TestBMWDataAnalyzer::test_initialization -v
```

## Test Categories

### Unit Tests
Test individual components in isolation:
- `test_data_analyzer.py` - Data analysis functions
- `test_llm_provider.py` - LLM provider abstraction
- `test_report_evaluator.py` - Report quality evaluation

### Integration Tests
Test component interactions (to be implemented):
- End-to-end workflow
- API integrations
- File I/O operations

## Code Coverage

Target: **>80% code coverage**

View coverage report:
```bash
# Generate HTML report
pytest --cov=. --cov-report=html

# Open in browser
start htmlcov/index.html  # Windows
open htmlcov/index.html   # macOS
```

## Continuous Integration

Tests run automatically on:
- Push to `main` or `develop` branches
- Pull requests

See `.github/workflows/ci.yml` for CI configuration.

## Writing Tests

### Test Naming Convention
- Test files: `test_*.py`
- Test classes: `Test*`
- Test methods: `test_*`

### Example Test
```python
import unittest
from my_module import MyClass

class TestMyClass(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.obj = MyClass()
    
    def test_my_method(self):
        """Test my_method functionality"""
        result = self.obj.my_method()
        self.assertEqual(result, expected_value)
```

### Best Practices
1. **Test isolation** - Each test should be independent
2. **Use fixtures** - Set up common test data in `setUp()`
3. **Mock external dependencies** - Use `unittest.mock` for APIs
4. **Clear assertions** - Use descriptive assertion messages
5. **Test edge cases** - Include boundary and error conditions

## Mocking LLM APIs

Since LLM API calls are expensive and require credentials, we mock them in tests:

```python
from unittest.mock import patch, Mock

@patch('llm_provider.OpenAI')
def test_with_mock_openai(self, mock_openai):
    # Test code here
    pass
```

## Test Data

Test data is generated programmatically in test fixtures:
- See `TestBMWDataAnalyzer.setUpClass()` for example
- Avoid committing large test data files

## Performance Testing

For performance-critical code:
```python
import time

def test_performance(self):
    start = time.time()
    result = expensive_function()
    duration = time.time() - start
    self.assertLess(duration, 1.0)  # Should complete in <1s
```

## Debugging Tests

### Run with verbose output
```bash
pytest -v -s
```

### Run with debugger
```bash
pytest --pdb
```

### Run only failed tests
```bash
pytest --lf
```

## Pre-commit Testing

Recommended: Run tests before committing:
```bash
make test
make lint
```

Or set up pre-commit hooks:
```bash
pip install pre-commit
pre-commit install
```

## Test Maintenance

- Update tests when changing functionality
- Keep test coverage above 80%
- Review and update mocks when APIs change
- Document complex test scenarios
