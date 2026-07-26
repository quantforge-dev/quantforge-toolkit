# QuantForge Risk Toolkit

Professional open-source risk management toolkit for traders and investors.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Tests](https://github.com/quantforge-dev/quantforge-toolkit/actions/workflows/python-tests.yml/badge.svg)

---

## Overview

QuantForge Risk Toolkit is an open-source Python project focused on practical
risk management utilities for financial markets.

The project emphasizes:

- Clean architecture
- Reliable financial calculations
- Reusable modules
- Professional documentation
- Automated testing using GitHub Actions

The toolkit is being developed as a long-term project and will continue to
expand with additional quantitative finance tools.

---

# Features

Current modules include:

- Risk Amount Calculator
- Position Size Calculator
- Risk / Reward Calculator
- Portfolio Allocation
- Portfolio Summary
- Drawdown Calculator
- Sharpe Ratio Calculator

---

# Project Structure

```
quantforge-toolkit/
│
├── app/
├── calculators/
├── models/
├── tests/
├── validation/
│
├── README.md
├── LICENSE
├── CHANGELOG.md
└── requirements.txt
```

---

# Example

```python
from calculators.risk_amount import calculate_risk_amount

risk = calculate_risk_amount(
    account_balance=10000,
    risk_percent=1,
)

print(risk)

# Output:
# 100.0
```

---

# Running Tests

Execute all unit tests with:

```bash
python -m unittest discover
```

GitHub Actions automatically runs the complete test suite on every push.

---

# Design Principles

- Capital preservation first
- Risk-aware calculations
- Modular architecture
- Clear documentation
- Clean code
- Automated testing

---

# Roadmap

### Version 1.x

- Portfolio Metrics
- Volatility Calculator
- Kelly Criterion
- Value at Risk (VaR)
- Expected Shortfall
- Monte Carlo Simulation
- Performance Metrics

---

# Contributing

Contributions, suggestions and pull requests are welcome.

---

# License

Released under the MIT License.
