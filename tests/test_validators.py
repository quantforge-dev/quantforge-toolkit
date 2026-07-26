import unittest

from validation.validators import (
    validate_not_empty,
    validate_non_negative,
    validate_percentage,
    validate_positive,
)


class TestValidators(unittest.TestCase):

    def test_positive(self):
        validate_positive(10, "Value")

    def test_invalid_positive(self):
        with self.assertRaises(ValueError):
            validate_positive(0, "Value")

    def test_non_negative(self):
        validate_non_negative(0, "Value")

    def test_invalid_non_negative(self):
        with self.assertRaises(ValueError):
            validate_non_negative(-1, "Value")

    def test_percentage(self):
        validate_percentage(50, "Percentage")

    def test_invalid_percentage(self):
        with self.assertRaises(ValueError):
            validate_percentage(101, "Percentage")

    def test_not_empty(self):
        validate_not_empty([1], "Collection")

    def test_empty(self):
        with self.assertRaises(ValueError):
            validate_not_empty([], "Collection")


if __name__ == "__main__":
    unittest.main()
