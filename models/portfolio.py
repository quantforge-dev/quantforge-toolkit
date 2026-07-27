"""
Portfolio Model.
"""


class Portfolio:
    """
    Represents a portfolio of assets.
    """

    def __init__(
        self,
        returns: dict,
        weights: dict,
        volatilities: dict,
    ):
        self.returns = returns
        self.weights = weights
        self.volatilities = volatilities

    @property
    def assets(self):
        return list(self.weights.keys())

    @property
    def asset_count(self):
        return len(self.weights)
