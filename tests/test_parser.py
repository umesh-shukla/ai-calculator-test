"""Unit tests for calculator parser module."""

import unittest

from calculator.parser import parse_number, parse_operator, parse_args


class TestParseNumber(unittest.TestCase):
    """Tests for the parse_number function."""

    def test_parse_positive_integer(self):
        self.assertEqual(parse_number("5"), 5.0)

    def test_parse_negative_integer(self):
        self.assertEqual(parse_number("-5"), -5.0)

    def test_parse_positive_float(self):
        self.assertEqual(parse_number("3.14"), 3.14)

    def test_parse_negative_float(self):
        self.assertEqual(parse_number("-3.14"), -3.14)

    def test_parse_zero(self):
        self.assertEqual(parse_number("0"), 0.0)

    def test_parse_invalid_string(self):
        with self.assertRaises(ValueError) as context:
            parse_number("abc")
        self.assertEqual(str(context.exception), "Invalid input")

    def test_parse_empty_string(self):
        with self.assertRaises(ValueError) as context:
            parse_number("")
        self.assertEqual(str(context.exception), "Invalid input")

    def test_parse_mixed_invalid(self):
        with self.assertRaises(ValueError) as context:
            parse_number("12abc")
        self.assertEqual(str(context.exception), "Invalid input")


class TestParseOperator(unittest.TestCase):
    """Tests for the parse_operator function."""

    def test_parse_addition(self):
        self.assertEqual(parse_operator("+"), "+")

    def test_parse_subtraction(self):
        self.assertEqual(parse_operator("-"), "-")

    def test_parse_multiplication(self):
        self.assertEqual(parse_operator("*"), "*")

    def test_parse_division(self):
        self.assertEqual(parse_operator("/"), "/")

    def test_parse_invalid_operator(self):
        with self.assertRaises(ValueError) as context:
            parse_operator("%")
        self.assertEqual(str(context.exception), "Unsupported operator '%'")

    def test_parse_invalid_operator_word(self):
        with self.assertRaises(ValueError) as context:
            parse_operator("plus")
        self.assertEqual(str(context.exception), "Unsupported operator 'plus'")

    def test_parse_empty_operator(self):
        with self.assertRaises(ValueError) as context:
            parse_operator("")
        self.assertEqual(str(context.exception), "Unsupported operator ''")


class TestParseArgs(unittest.TestCase):
    """Tests for the parse_args function."""

    def test_parse_valid_addition(self):
        result = parse_args(["10", "+", "5"])
        self.assertEqual(result, (10.0, "+", 5.0))

    def test_parse_valid_subtraction(self):
        result = parse_args(["10", "-", "5"])
        self.assertEqual(result, (10.0, "-", 5.0))

    def test_parse_valid_multiplication(self):
        result = parse_args(["10", "*", "5"])
        self.assertEqual(result, (10.0, "*", 5.0))

    def test_parse_valid_division(self):
        result = parse_args(["10", "/", "5"])
        self.assertEqual(result, (10.0, "/", 5.0))

    def test_parse_with_floats(self):
        result = parse_args(["3.14", "+", "2.86"])
        self.assertEqual(result, (3.14, "+", 2.86))

    def test_parse_with_negative_numbers(self):
        result = parse_args(["-10", "+", "-5"])
        self.assertEqual(result, (-10.0, "+", -5.0))

    def test_parse_too_few_args(self):
        with self.assertRaises(ValueError) as context:
            parse_args(["10", "+"])
        self.assertEqual(str(context.exception), "Invalid input")

    def test_parse_too_many_args(self):
        with self.assertRaises(ValueError) as context:
            parse_args(["10", "+", "5", "extra"])
        self.assertEqual(str(context.exception), "Invalid input")

    def test_parse_no_args(self):
        with self.assertRaises(ValueError) as context:
            parse_args([])
        self.assertEqual(str(context.exception), "Invalid input")

    def test_parse_invalid_first_number(self):
        with self.assertRaises(ValueError) as context:
            parse_args(["abc", "+", "5"])
        self.assertEqual(str(context.exception), "Invalid input")

    def test_parse_invalid_second_number(self):
        with self.assertRaises(ValueError) as context:
            parse_args(["10", "+", "xyz"])
        self.assertEqual(str(context.exception), "Invalid input")

    def test_parse_invalid_operator_in_args(self):
        with self.assertRaises(ValueError) as context:
            parse_args(["10", "%", "5"])
        self.assertEqual(str(context.exception), "Unsupported operator '%'")


if __name__ == "__main__":
    unittest.main()
