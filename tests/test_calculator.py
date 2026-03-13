"""Tests for the main calculator CLI entry point."""

import importlib.util
import os
import sys
from io import StringIO
from unittest import TestCase, main
from unittest.mock import patch

# Load calculator.py from the project root (not the calculator package)
spec = importlib.util.spec_from_file_location(
    "calculator_cli",
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "calculator.py")
)
calculator_cli = importlib.util.module_from_spec(spec)
spec.loader.exec_module(calculator_cli)

calculate = calculator_cli.calculate
calculator_main = calculator_cli.main


class TestCalculate(TestCase):
    """Tests for the calculate function."""

    def test_addition(self):
        """Test addition operation."""
        self.assertEqual(calculate(10, '+', 5), 15.0)

    def test_subtraction(self):
        """Test subtraction operation."""
        self.assertEqual(calculate(10, '-', 5), 5.0)

    def test_multiplication(self):
        """Test multiplication operation."""
        self.assertEqual(calculate(10, '*', 5), 50.0)

    def test_division(self):
        """Test division operation."""
        self.assertEqual(calculate(10, '/', 5), 2.0)

    def test_division_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            calculate(10, '/', 0)
        self.assertEqual(str(context.exception), "Division by zero")

    def test_invalid_operator(self):
        """Test invalid operator raises ValueError."""
        with self.assertRaises(ValueError) as context:
            calculate(10, '%', 5)
        self.assertEqual(str(context.exception), "Unsupported operator '%'")


class TestMain(TestCase):
    """Tests for the main CLI function."""

    def test_addition_cli(self):
        """Test addition via CLI."""
        with patch.object(sys, 'argv', ['calculator.py', '10', '+', '5']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                result = calculator_main()
                self.assertEqual(result, 0)
                self.assertEqual(mock_stdout.getvalue().strip(), "Result: 15.0")

    def test_subtraction_cli(self):
        """Test subtraction via CLI."""
        with patch.object(sys, 'argv', ['calculator.py', '10', '-', '5']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                result = calculator_main()
                self.assertEqual(result, 0)
                self.assertEqual(mock_stdout.getvalue().strip(), "Result: 5.0")

    def test_multiplication_cli(self):
        """Test multiplication via CLI."""
        with patch.object(sys, 'argv', ['calculator.py', '10', '*', '5']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                result = calculator_main()
                self.assertEqual(result, 0)
                self.assertEqual(mock_stdout.getvalue().strip(), "Result: 50.0")

    def test_division_cli(self):
        """Test division via CLI."""
        with patch.object(sys, 'argv', ['calculator.py', '10', '/', '5']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                result = calculator_main()
                self.assertEqual(result, 0)
                self.assertEqual(mock_stdout.getvalue().strip(), "Result: 2.0")

    def test_division_by_zero_cli(self):
        """Test division by zero error handling via CLI."""
        with patch.object(sys, 'argv', ['calculator.py', '10', '/', '0']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                result = calculator_main()
                self.assertEqual(result, 1)
                self.assertEqual(mock_stdout.getvalue().strip(), "Error: Division by zero")

    def test_invalid_operator_cli(self):
        """Test invalid operator error handling via CLI."""
        with patch.object(sys, 'argv', ['calculator.py', '10', '%', '5']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                result = calculator_main()
                self.assertEqual(result, 1)
                self.assertEqual(mock_stdout.getvalue().strip(), "Error: Unsupported operator '%'")

    def test_invalid_input_non_numeric(self):
        """Test invalid input with non-numeric value."""
        with patch.object(sys, 'argv', ['calculator.py', 'abc', '+', '5']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                result = calculator_main()
                self.assertEqual(result, 1)
                self.assertEqual(mock_stdout.getvalue().strip(), "Error: Invalid input")

    def test_invalid_input_missing_args(self):
        """Test invalid input with missing arguments."""
        with patch.object(sys, 'argv', ['calculator.py', '10', '+']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                result = calculator_main()
                self.assertEqual(result, 1)
                self.assertEqual(mock_stdout.getvalue().strip(), "Error: Invalid input")

    def test_invalid_input_no_args(self):
        """Test invalid input with no arguments."""
        with patch.object(sys, 'argv', ['calculator.py']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                result = calculator_main()
                self.assertEqual(result, 1)
                self.assertEqual(mock_stdout.getvalue().strip(), "Error: Invalid input")


if __name__ == "__main__":
    main()
