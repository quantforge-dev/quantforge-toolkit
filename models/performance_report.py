"""
Performance Report.
"""

from models.backtest_result import (
    BacktestResult,
)


class PerformanceReport:

    """
    Generate a summary report.
    """

    def __init__(
        self,
        result: BacktestResult,
    ):

        self.result = result

    def summary(self):

        return {

            "Initial Capital":
                self.result.initial_capital,

            "Final Capital":
                self.result.final_capital,

            "Total Return (%)":
                self.result.total_return,

            "Max Drawdown (%)":
                self.result.max_drawdown,

            "Sharpe Ratio":
                self.result.sharpe_ratio,

        }
