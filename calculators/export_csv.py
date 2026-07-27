"""
CSV Export Utilities.
"""

import csv


def export_csv(
    data,
    file_path,
):
    """
    Export a list of dictionaries
    to CSV.
    """

    if not data:
        raise ValueError(
            "Data cannot be empty."
        )

    with open(
        file_path,
        "w",
        newline="",
        encoding="utf-8",
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=data[0].keys(),
        )

        writer.writeheader()

        writer.writerows(
            data
        )
