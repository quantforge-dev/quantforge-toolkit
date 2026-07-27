"""
Portfolio Constraints.
"""


def validate_weights(
    weights: dict,
):
    """
    Validate portfolio weights.
    """

    total = round(
        sum(weights.values()),
        2,
    )

    if total != 100:
        raise ValueError(
            "Weights must total 100."
        )

    for value in weights.values():

        if value < 0:

            raise ValueError(
                "Negative weights are not allowed."
            )

    return True
