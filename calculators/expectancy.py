"""
Trade Expectancy Calculator.
"""

from validation.validators import validate_percentage, validate_positive


def calculate_expectancy(
    win_rate: float,
    average_win: float,
    average_loss: float,
) -> float:
    """
    Calculate trade expectancy.
    """

    validate_percentage(win_rate, "Win rate")
    validate_positive(average_win, "Average win")
    validate_positive(average_loss, "Average loss")

    loss_rate = 100 - win_rate

    expectancy = (
        (win_rate / 100) * average_win
        - (loss_rate / 100) * average_loss
    )

    return round(expectancy, 2)
