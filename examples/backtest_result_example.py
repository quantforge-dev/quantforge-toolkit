from models.backtest_result import (
    BacktestResult,
)

result = BacktestResult(

    10000,

    12000,

    20,

    7,

    1.5,
)

print(
    result.to_dict()
)
