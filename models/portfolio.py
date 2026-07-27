"""
Portfolio Model.
"""


class Portfolio:
    """
    Represents an investment portfolio.
    """

    def __init__(
        self,
        name: str,
        returns: dict,
        weights: dict,
        volatilities: dict,
    ):
        self.name = name
        self.returns = returns
        self.weights = weights
        self.volatilities = volatilities

    @property
    def assets(self):
        """
        Return portfolio asset names.
        """
        return list(self.weights.keys())

    @property
    def asset_count(self):
        """
        Number of assets.
        """
        return len(self.weights)

    @property
    def total_weight(self):
        """
        Sum of portfolio weights.
        """
        return round(
            sum(self.weights.values()),
            2,
        )

    def to_dict(self):
        """
        Convert portfolio to dictionary.
        """
        return {
            "name": self.name,
            "returns": self.returns,
            "weights": self.weights,
            "volatilities": self.volatilities,
        }
