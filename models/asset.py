"""
Asset data model.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Asset:
    """
    Represents a financial asset.

    Attributes:
        name:
            Asset name.

        value:
            Monetary value of the asset.
    """

    name: str
    value: float
