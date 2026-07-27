"""
Expected Shortfall (CVaR) Calculator.
"""


def expected_shortfall(
    value_at_risk: float,
    stress_multiplier: float,
):
    """
    Estimate Expected Shortfall.
    """

    if value_at_risk <= 0:
        raise ValueError(
            "VaR must be positive."
        )

    if stress_multiplier < 1:
        raise ValueError(
            "Stress multiplier must be at least 1."
        )

    return round(
        value_at_risk * stress_multiplier,
        2,
    )
