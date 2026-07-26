"""
Portfolio Return Calculator.
"""


def calculate_portfolio_return(
    returns: dict,
) -> float:
    """
    Calculate total portfolio return.
    """

    if not returns:
        raise ValueError(
            "Portfolio cannot be empty."
        )

    return round(
        sum(returns.values()),
        2,
    )
