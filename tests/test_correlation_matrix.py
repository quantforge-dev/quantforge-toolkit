import unittest

from calculators.correlation_matrix import (
    validate_correlation_matrix,
)


class TestCorrelationMatrix(unittest.TestCase):

    def test_valid_matrix(self):
        matrix = [
            [1, 0.5],
            [0.5, 1],
        ]

        result = validate_correlation_matrix(matrix)

        self.assertTrue(result["is_valid"])
        self.assertEqual(result["size"], 2)

    def test_empty_matrix(self):
        with self.assertRaises(ValueError):
            validate_correlation_matrix([])

    def test_non_square_matrix(self):
        matrix = [
            [1, 0.5],
            [0.5],
        ]

        with self.assertRaises(ValueError):
            validate_correlation_matrix(matrix)


if __name__ == "__main__":
    unittest.main()
