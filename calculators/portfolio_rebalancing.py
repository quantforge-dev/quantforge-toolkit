"""
Portfolio Rebalancing Utilities.
"""


def rebalance_portfolio(
    current_weights: dict,
    target_weights: dict,
):
    """
    Calculate required portfolio rebalancing.
    """

    if set(current_weights.keys()) != set(
        target_weights.keys()
    ):
        raise ValueError(
            "Assets must match."
        )

    adjustments = {}

    for asset in current_weights:

        adjustments[asset] = round(
            target_weights[asset]
            - current_weights[asset],
            2,
        )

    return adjustments
