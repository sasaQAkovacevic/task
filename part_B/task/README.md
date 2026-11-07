# Simple Automation Framework

## Overview

This is a simple example of automation framework for web application. 
One API test and one UI test are implemented.

## Application URL

https://qae-assignment-tau.vercel.app/

## Project Structure

```
task/
├── api_tests/                          # API tests folder
│   └── test_balance.py                 # API test for checking balance calculation
├── clients/                            # API calls folder (API calls and test data)
│   └── clients.py                      # API methods used in test
├── pages/                              # page folder (locators and methods used on UI and test data)
│   └── bet_page.py                     # locators and methods used in test
├── reports/                            # reports folder
│   └── report.html                     # last pytest-html report
├── ui_tests/                           # UI tests folder
│   └── bet_test.py                     # UI test for checking placing bet flow
├── conftest.py                         # pytest fixtures
├── README.md                           # This file
└── requirements.txt                    # Python dependencies

```

## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Chrome browser

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

### Run All Tests
```bash
pytest
```

### Run with Verbose Output
```bash
pytest -v
```

### Run tests with html report as output
```bash
pytest --html=reports/report.html --self-contained-html
```

## Test Reports
After test execution, HTML report is generated in the `reports/` folder:
- `report.html`

View the report:
```bash
open reports/report.html
```

## Questions or help:
Ping author: Sasa Kovacevic sasakovacevic@eunet.rs
