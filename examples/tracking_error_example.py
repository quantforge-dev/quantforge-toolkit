from calculators.tracking_error import (
    calculate_tracking_error,
)

active_returns = [
    0.01,
    -0.01,
    0.02,
    0.03,
]

print(
    calculate_tracking_error(
        active_returns
    )
)
