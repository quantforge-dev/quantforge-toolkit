"""
Risk Budget Calculator.

Normalize portfolio weights
into risk budget percentages.
"""


def risk_budget(weights):
    """
    Convert portfolio weights
    into normalized risk budgets.

    Parameters
    ----------
    weights : list[float]

    Returns
    -------
    list[float]
    """

    if not weights:
        raise ValueError(
            "Weights cannot be empty."
        )

    total = sum(weights)

    if total <= 0:
        raise ValueError(
            "Total weight must be positive."
        )

    return [
        round(
            weight / total,
            4,
        )
        for weight in weights
    ]
