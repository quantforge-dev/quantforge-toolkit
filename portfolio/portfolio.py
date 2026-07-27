"""
Portfolio model.
"""

from portfolio.asset import Asset


class Portfolio:

    def __init__(self):
        self.assets = []

    def add_asset(
        self,
        symbol,
        weight,
    ):
        self.assets.append(
            Asset(symbol, weight)
        )

    def total_weight(self):
        return round(
            sum(
                asset.weight
                for asset in self.assets
            ),
            4,
        )

    def __len__(self):
        return len(self.assets)
