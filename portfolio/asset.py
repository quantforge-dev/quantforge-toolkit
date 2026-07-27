"""
Asset model.
"""


class Asset:

    def __init__(
        self,
        symbol,
        weight,
    ):
        self.symbol = symbol
        self.weight = weight

    def __repr__(self):
        return (
            f"Asset("
            f"{self.symbol}, "
            f"{self.weight})"
        )
