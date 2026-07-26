"""
Maximum Drawdown Calculator.
"""


def calculate_maximum_drawdown(
    equity_curve: list[float],
) -> float:
    """
    Calculate maximum drawdown.
    """

    if not equity_curve:
        raise ValueError(
            "Equity curve cannot be empty."
        )

    peak = equity_curve[0]
    max_drawdown = 0.0

    for value in equity_curve:

        if value > peak:
            peak = value

        drawdown = (
            (peak - value)
            / peak
        ) * 100

        max_drawdown = max(
            max_drawdown,
            drawdown,
        )

    return round(
        max_drawdown,
        2,
    )
