"""
Portfolio Validator.
"""


def validate_portfolio(
    portfolio,
):

    if (
        set(portfolio.returns.keys())
        != set(portfolio.weights.keys())
        or
        set(portfolio.weights.keys())
        != set(portfolio.volatilities.keys())
    ):
        raise ValueError(
            "Portfolio assets must match."
        )

    total = round(
        sum(
            portfolio.weights.values()
        ),
        2,
    )

    if total != 100:
        raise ValueError(
            "Weights must total 100."
        )

    return True
