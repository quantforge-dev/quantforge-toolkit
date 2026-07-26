"""
Portfolio data model.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Portfolio:
    """
    Represents a financial portfolio.
    """

    name: str
    assets: dict[str, float]
