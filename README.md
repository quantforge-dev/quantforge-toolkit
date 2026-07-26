# QuantForge Risk Toolkit

Professional open-source risk management toolkit for traders and investors.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Tests](https://github.com/quantforge-dev/quantforge-toolkit/actions/workflows/python-tests.yml/badge.svg)

---

## Overview

QuantForge Risk Toolkit is an open-source Python toolkit focused on practical
risk management and portfolio analytics for financial markets.

The project is designed with clean architecture, modular components, automated
testing, and professional documentation to serve as a reusable quantitative
finance toolkit.

---

## Features

Current modules include:

- Risk Amount Calculator
- Position Size Calculator
- Risk / Reward Calculator
- Drawdown Calculator
- Portfolio Allocation Calculator
- Portfolio Summary Calculator
- Portfolio Volatility Calculator
- Sharpe Ratio Calculator
- Profit / Loss Calculator
- Break-even Calculator
- Compound Growth Calculator
- Expectancy Calculator
- Kelly Criterion Calculator

---

## Project Structure

```text
quantforge-toolkit/
│
├── app/
├── calculators/
├── models/
├── tests/
├── validation/
│
├── README.md
├── CHANGELOG.md
├── LICENSE
├── requirements.txt
```

---

## Running Tests

```bash
python -m unittest discover
```

GitHub Actions automatically executes all unit tests on every push.

---

## Design Principles

- Modular architecture
- Reusable components
- Strong input validation
- Reliable financial calculations
- Automated testing
- Clean documentation

---

## Supported Markets

The toolkit is designed to be market-agnostic and supports calculations for:

- Cryptocurrency
- Forex
- Stocks
- ETFs
- Commodities
- Bonds
- Futures

---

## Roadmap

### Version 1.x

- Improve portfolio analytics
- Improve validation
- Additional performance metrics

### Version 2.x

- Variance
- Volatility
- Correlation
- Covariance Matrix
- Value at Risk (VaR)
- Expected Shortfall (CVaR)
- Diversification Metrics
- Rolling Volatility
- Rolling Sharpe Ratio
- Scenario Analysis
- Stress Testing

---

## Contributing

Contributions, suggestions, and pull requests are welcome.

---

## License

Released under the MIT License.
