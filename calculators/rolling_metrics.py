"""
Rolling Metrics

Rolling calculations for financial time series.
"""

from validation.validators import validate_positive


def rolling_mean(values, window):
    """
    Calculate rolling mean.
    """

    validate_positive(window, "Window")

    if len(values) < window:
        raise ValueError(
            "Window cannot be larger than data length."
        )

    result = []

    for i in range(len(values) - window + 1):
        chunk = values[i:i + window]
        result.append(round(sum(chunk) / window, 4))

    return result


def rolling_return(values, window):
    """
    Calculate rolling returns.
    """

    validate_positive(window, "Window")

    if len(values) < window:
        raise ValueError(
            "Window cannot be larger than data length."
        )

    returns = []

    for i in range(len(values) - window):
        first = values[i]
        last = values[i + window]

        returns.append(
            round((last - first) / first, 4)
        )

    return returns
