from models.backtest_result import (
    BacktestResult,
)

from models.performance_report import (
    PerformanceReport,
)

result = BacktestResult(

    10000,

    12000,

    20,

    7,

    1.5,
)

report = PerformanceReport(
    result
)

print(
    report.summary()
)
