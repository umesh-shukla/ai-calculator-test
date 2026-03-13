"""Unit tests for calculator operations."""

import unittest

from calculator.operations import add, subtract, multiply, divide


class TestAdd(unittest.TestCase):
    """Tests for the add function."""

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-2, 3), 1)

    def test_add_floats(self):
        self.assertAlmostEqual(add(2.5, 3.5), 6.0)

    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)


class TestSubtract(unittest.TestCase):
    """Tests for the subtract function."""

    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-5, -3), -2)

    def test_subtract_mixed_numbers(self):
        self.assertEqual(subtract(-2, 3), -5)

    def test_subtract_floats(self):
        self.assertAlmostEqual(subtract(5.5, 2.5), 3.0)

    def test_subtract_zero(self):
        self.assertEqual(subtract(5, 0), 5)


class TestMultiply(unittest.TestCase):
    """Tests for the multiply function."""

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-2, -3), 6)

    def test_multiply_mixed_numbers(self):
        self.assertEqual(multiply(-2, 3), -6)

    def test_multiply_floats(self):
        self.assertAlmostEqual(multiply(2.5, 4), 10.0)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(5, 0), 0)


class TestDivide(unittest.TestCase):
    """Tests for the divide function."""

    def test_divide_positive_numbers(self):
        self.assertEqual(divide(6, 3), 2)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-6, -3), 2)

    def test_divide_mixed_numbers(self):
        self.assertEqual(divide(-6, 3), -2)

    def test_divide_floats(self):
        self.assertAlmostEqual(divide(7.5, 2.5), 3.0)

    def test_divide_returns_float(self):
        result = divide(5, 2)
        self.assertEqual(result, 2.5)
        self.assertIsInstance(result, float)

    def test_divide_by_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            divide(5, 0)
        self.assertEqual(str(context.exception), "Division by zero")

    def test_divide_zero_by_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            divide(0, 0)
        self.assertEqual(str(context.exception), "Division by zero")


if __name__ == "__main__":
    unittest.main()
