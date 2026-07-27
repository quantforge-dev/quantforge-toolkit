"""
Monte Carlo Simulation

Simulate possible future portfolio values using
normally distributed returns.
"""

import random
import statistics

from validation.validators import validate_positive


def monte_carlo_simulation(
    initial_value: float,
    expected_return: float,
    volatility: float,
    simulations: int = 1000,
):
    """
    Run a Monte Carlo simulation.

    Parameters
    ----------
    initial_value : float
        Initial portfolio value.

    expected_return : float
        Expected return per period.

    volatility : float
        Expected volatility per period.

    simulations : int
        Number of simulations.

    Returns
    -------
    dict
        Simulation statistics.
    """

    validate_positive(initial_value, "Initial value")
    validate_positive(volatility, "Volatility")
    validate_positive(simulations, "Simulations")

    results = []

    for _ in range(simulations):
        random_return = random.gauss(
            expected_return,
            volatility,
        )

        final_value = initial_value * (1 + random_return)

        results.append(final_value)

    return {
        "mean": round(statistics.mean(results), 2),
        "minimum": round(min(results), 2),
        "maximum": round(max(results), 2),
        "median": round(statistics.median(results), 2),
    }
