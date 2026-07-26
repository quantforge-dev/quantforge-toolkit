"""
Covariance Calculator.
"""


def calculate_covariance(
    x: list[float],
    y: list[float],
) -> float:
    """
    Calculate population covariance.
    """

    if len(x) != len(y):
        raise ValueError(
            "Series must have equal length."
        )

    if not x:
        raise ValueError(
            "Series cannot be empty."
        )

    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)

    covariance = sum(
        (
            (a - mean_x)
            * (b - mean_y)
        )
        for a, b in zip(x, y)
    ) / len(x)

    return round(
        covariance,
        8,
    )
