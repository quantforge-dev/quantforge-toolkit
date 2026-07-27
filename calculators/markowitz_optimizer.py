"""
Markowitz Portfolio Optimizer.

Select the portfolio with the highest
return-to-risk ratio.
"""


def markowitz_optimizer(portfolios: list) -> dict:
    """
    Select the portfolio with the
    highest return/risk score.

    Parameters
    ----------
    portfolios : list

        Example:

        [
            {
                "return": 12,
                "volatility": 8,
                "weights": {...}
            }
        ]

    Returns
    -------
    dict
        Best portfolio.
    """

    if not portfolios:
        raise ValueError(
            "Portfolio list cannot be empty."
        )

    best = None
    best_score = float("-inf")

    for portfolio in portfolios:

        volatility = portfolio["volatility"]

        if volatility <= 0:
            continue

        score = (
            portfolio["return"]
            / volatility
        )

        if score > best_score:
            best_score = score
            best = portfolio

    if best is None:
        raise ValueError(
            "No valid portfolio found."
        )

    return best
