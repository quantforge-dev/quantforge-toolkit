"""
Risk Budget Utilities
"""


def risk_budget(weights):
    """
    Normalize weights into
    risk budget percentages.
    """

    total = sum(weights)

    return [
        round(
            weight / total,
            4,
        )
        for weight in weights
    ]
