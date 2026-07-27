"""
Portfolio Performance Metrics.
"""


def performance_metrics(
    portfolio_return: float,
    benchmark_return: float,
):
    """
    Generate a basic performance summary.
    """

    active_return = (
        portfolio_return
        - benchmark_return
    )

    return {
        "portfolio_return": portfolio_return,
        "benchmark_return": benchmark_return,
        "active_return": round(
            active_return,
            4,
        ),
    }
