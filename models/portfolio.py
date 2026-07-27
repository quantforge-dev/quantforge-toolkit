"""
Portfolio Model.
"""


class Portfolio:
    """
    Represents a portfolio of assets.
    """

    def __init__(
        self,
        name: str,
        assets: dict,
    ):
        self.name = name
        self.assets = assets

    @property
    def asset_count(self):
        """
        Number of assets.
        """
        return len(self.assets)

    @property
    def total_weight(self):
        """
        Total portfolio weight.
        """
        return round(
            sum(self.assets.values()),
            2,
        )

    def to_dict(self):
        """
        Convert portfolio to dictionary.
        """
        return {
            "name": self.name,
            "assets": self.assets,
        }
