"""Main CLI entry point for the calculator."""

import sys

from calculator.operations import add, subtract, multiply, divide
from calculator.parser import parse_args


def calculate(num1: float, operator: str, num2: float) -> float:
    """Execute the appropriate operation based on the operator.

    Args:
        num1: First number.
        operator: The operator (+, -, *, /).
        num2: Second number.

    Returns:
        The result of the calculation.

    Raises:
        ValueError: If the operator is not supported.
    """
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }

    operation = operations.get(operator)
    if operation is None:
        raise ValueError(f"Unsupported operator '{operator}'")

    return operation(num1, num2)


def main() -> int:
    """Main entry point for the calculator CLI.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    try:
        num1, operator, num2 = parse_args(sys.argv[1:])
        result = calculate(num1, operator, num2)
        print(f"Result: {result}")
        return 0
    except ValueError as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
