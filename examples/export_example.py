from calculators.export_json import (
    export_json,
)

from calculators.export_csv import (
    export_csv,
)

portfolio = {

    "return": 12,

    "risk": 8,
}

export_json(
    portfolio,
    "portfolio.json",
)

export_csv(
    [portfolio],
    "portfolio.csv",
)
