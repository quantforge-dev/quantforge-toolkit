"""
Correlation Matrix Utilities.

Provides simple validation utilities for correlation matrices.
"""


def validate_correlation_matrix(matrix):
    """
    Validate a correlation matrix.

    Returns
    -------
    dict
    """

    if not matrix:
        raise ValueError(
            "Correlation matrix cannot be empty."
        )

    size = len(matrix)

    for row in matrix:
        if len(row) != size:
            raise ValueError(
                "Matrix must be square."
            )

    return {
        "size": size,
        "is_valid": True,
    }
