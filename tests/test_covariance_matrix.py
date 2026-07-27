import unittest

from calculators.covariance_matrix import (
    covariance_summary,
)


class TestCovarianceMatrix(unittest.TestCase):

    def test_valid_matrix(self):
        matrix = [
            [1, 2],
            [2, 3],
        ]

        result = covariance_summary(matrix)

        self.assertEqual(result["rows"], 2)
        self.assertEqual(result["columns"], 2)

    def test_empty_matrix(self):
        with self.assertRaises(ValueError):
            covariance_summary([])


if __name__ == "__main__":
    unittest.main()
