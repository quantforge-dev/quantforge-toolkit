"""
Efficient Frontier Statistics.
"""


def frontier_statistics(
    frontier,
):
    """
    Calculate frontier statistics.
    """

    if not frontier:

        raise ValueError(
            "Frontier cannot be empty."
        )

    returns = [

        x["return"]

        for x in frontier

    ]

    volatility = [

        x["volatility"]

        for x in frontier

    ]

    return {

        "max_return":
        max(returns),

        "min_return":
        min(returns),

        "max_volatility":
        max(volatility),

        "min_volatility":
        min(volatility),

    }
