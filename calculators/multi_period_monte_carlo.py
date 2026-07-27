"""
Multi-period Monte Carlo Simulation.
"""

import random


def multi_period_monte_carlo(
    initial_value: float,
    expected_return: float,
    volatility: float,
    periods: int,
):
    """
    Simulate portfolio value
    over multiple periods.

    Returns
    -------
    list[float]
    """

    if initial_value <= 0:
        raise ValueError(
            "Initial value must be positive."
        )

    if volatility < 0:
        raise ValueError(
            "Volatility cannot be negative."
        )

    if periods <= 0:
        raise ValueError(
            "Periods must be positive."
        )

    values = [initial_value]

    current = initial_value

    for _ in range(periods):

        shock = random.gauss(
            expected_return,
            volatility,
        )

        current *= (1 + shock)

        values.append(
            round(current, 2)
        )

    return values
