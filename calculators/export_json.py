"""
JSON Export Utilities.
"""

import json


def export_json(data, file_path):
    """
    Export data to a JSON file.

    Parameters
    ----------
    data : dict
        Data to export.

    file_path : str
        Output JSON file path.
    """

    with open(
        file_path,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
        )
