"""
Covariance Matrix Utilities.
"""


def covariance_summary(matrix):
    """
    Generate a summary of a covariance matrix.
    """

    if not matrix:
        raise ValueError(
            "Covariance matrix cannot be empty."
        )

    return {
        "rows": len(matrix),
        "columns": len(matrix[0]),
    }
