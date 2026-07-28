"""
Portfolio Validator.
"""


def validate_portfolio(
    portfolio,
):
    """
    Validate a Portfolio model.
    """

    if not portfolio.assets:

        raise ValueError(
            "Portfolio cannot be empty."
        )

    total = round(
        sum(
            portfolio.assets.values()
        ),
        2,
    )

    if total != 100:

        raise ValueError(
            "Asset weights must total 100."
        )

    for weight in portfolio.assets.values():

        if weight < 0:

            raise ValueError(
                "Negative weights are not allowed."
            )

    return True
