"""
Backtest Result Model.
"""


class BacktestResult:
    """
    Store summary statistics
    for a completed backtest.
    """

    def __init__(
        self,
        initial_capital,
        final_capital,
        total_return,
        max_drawdown,
        sharpe_ratio,
    ):

        self.initial_capital = initial_capital
        self.final_capital = final_capital
        self.total_return = total_return
        self.max_drawdown = max_drawdown
        self.sharpe_ratio = sharpe_ratio

    def to_dict(self):

        return {

            "initial_capital":
                self.initial_capital,

            "final_capital":
                self.final_capital,

            "total_return":
                self.total_return,

            "max_drawdown":
                self.max_drawdown,

            "sharpe_ratio":
                self.sharpe_ratio,
        }
