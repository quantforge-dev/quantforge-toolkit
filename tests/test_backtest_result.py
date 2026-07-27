import unittest

from models.backtest_result import (
    BacktestResult,
)


class TestBacktestResult(
    unittest.TestCase
):

    def test_to_dict(self):

        result = BacktestResult(

            initial_capital=10000,

            final_capital=12500,

            total_return=25,

            max_drawdown=8,

            sharpe_ratio=1.42,
        )

        self.assertEqual(

            result.to_dict(),

            {

                "initial_capital":10000,

                "final_capital":12500,

                "total_return":25,

                "max_drawdown":8,

                "sharpe_ratio":1.42,

            },

        )


if __name__ == "__main__":
    unittest.main()
