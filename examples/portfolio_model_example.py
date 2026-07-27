"""
Example: Portfolio Model
"""

from models.portfolio import Portfolio

portfolio = Portfolio(
    name="Demo Portfolio",
    assets={
        "Bitcoin": 50,
        "Gold": 30,
        "S&P 500 ETF": 20,
    },
)

print("Portfolio Name:")
print(portfolio.name)

print()

print("Assets:")
print(portfolio.assets)

print()

print("Number of Assets:")
print(portfolio.asset_count)

print()

print("Total Weight:")
print(portfolio.total_weight)

print()

print("Dictionary Representation:")
print(portfolio.to_dict())
