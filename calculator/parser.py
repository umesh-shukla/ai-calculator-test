"""Input parsing and validation for the calculator CLI."""

VALID_OPERATORS = ('+', '-', '*', '/')


def parse_number(value: str) -> float:
    """Convert a string to a float.

    Args:
        value: String representation of a number.

    Returns:
        The float value of the string.

    Raises:
        ValueError: If the string cannot be converted to a float.
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        raise ValueError("Invalid input")


def parse_operator(op: str) -> str:
    """Validate that the operator is supported.

    Args:
        op: The operator string.

    Returns:
        The validated operator.

    Raises:
        ValueError: If the operator is not one of +, -, *, /.
    """
    if op not in VALID_OPERATORS:
        raise ValueError(f"Unsupported operator '{op}'")
    return op


def parse_args(args: list) -> tuple:
    """Parse command line arguments into calculator inputs.

    Args:
        args: List of command line arguments (sys.argv[1:]).

    Returns:
        A tuple of (number1, operator, number2).

    Raises:
        ValueError: If the wrong number of arguments is provided,
                    or if any argument is invalid.
    """
    if len(args) != 3:
        raise ValueError("Invalid input")

    number1 = parse_number(args[0])
    operator = parse_operator(args[1])
    number2 = parse_number(args[2])

    return (number1, operator, number2)
