"""
Alpha Calculator.

Measures excess return relative to CAPM expectation.
"""


def calculate_alpha(
    portfolio_return: float,
    expected_return: float,
) -> float:
    """
    Calculate alpha.
    """

    return round(
        portfolio_return - expected_return,
        4,
    )
