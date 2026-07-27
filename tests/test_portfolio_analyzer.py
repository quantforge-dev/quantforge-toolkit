import unittest

from models.portfolio_analyzer import (
    PortfolioAnalyzer,
)


class TestPortfolioAnalyzer(
    unittest.TestCase
):

    def test_analysis(self):

        analyzer = PortfolioAnalyzer(

            returns={

                "BTC":12,

                "Gold":5,

            },

            weights={

                "BTC":50,

                "Gold":50,

            },

            volatilities={

                "BTC":0.25,

                "Gold":0.10,

            },

            risk_free_rate=2,

        )

        result = analyzer.analyze()

        self.assertIn(
            "return",
            result,
        )

        self.assertIn(
            "volatility",
            result,
        )

        self.assertIn(
            "sharpe_ratio",
            result,
        )


if __name__ == "__main__":
    unittest.main()
