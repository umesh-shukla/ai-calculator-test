"""Core arithmetic operations for the calculator."""


def add(a: float, b: float) -> float:
    """Add two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        The sum of a and b.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        The difference of a and b (a - b).
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        The product of a and b.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Divide two numbers.

    Args:
        a: Dividend.
        b: Divisor.

    Returns:
        The quotient of a and b (a / b).

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Division by zero")
    return a / b
