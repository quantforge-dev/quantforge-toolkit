import unittest

from calculators.random_portfolios import (
    generate_random_weights,
)


class TestRandomPortfolio(unittest.TestCase):

    def test_sum_of_weights(self):
        weights = generate_random_weights(8)

        self.assertAlmostEqual(
            sum(weights),
            1.0,
            places=4,
        )

        self.assertEqual(
            len(weights),
            8,
        )


if __name__ == "__main__":
    unittest.main()
