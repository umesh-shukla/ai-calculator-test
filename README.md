# Python CLI Calculator

A simple command-line calculator that supports basic arithmetic operations.

## Design Overview

The project follows a modular architecture with clear separation of concerns:

```
calculator.py          # Main CLI entry point
calculator/
    __init__.py
    operations.py      # Core arithmetic operations (add, subtract, multiply, divide)
    parser.py          # Input parsing and validation
tests/
    __init__.py
    test_calculator.py # Integration tests for the CLI
    test_operations.py # Unit tests for arithmetic operations
    test_parser.py     # Unit tests for input parsing
```

### Architecture

- **`calculator.py`**: The main entry point that handles CLI invocation. It parses command-line arguments, dispatches to the appropriate arithmetic operation, and outputs results or error messages.

- **`calculator/operations.py`**: Contains pure functions for the four arithmetic operations:
  - `add(a, b)` - Addition
  - `subtract(a, b)` - Subtraction
  - `multiply(a, b)` - Multiplication
  - `divide(a, b)` - Division (with zero-division protection)

- **`calculator/parser.py`**: Handles input validation and parsing:
  - `parse_number(value)` - Converts string input to float
  - `parse_operator(op)` - Validates the operator
  - `parse_args(args)` - Parses the full argument list

## Installation

No installation required. The calculator uses only Python standard library modules.

**Requirements:**
- Python 3

Simply clone or download the repository and run directly.

## Usage

Invoke the calculator from the command line:

```bash
python calculator.py <number1> <operator> <number2>
```

### Supported Operators

| Operator | Operation      |
|----------|----------------|
| `+`      | Addition       |
| `-`      | Subtraction    |
| `*`      | Multiplication |
| `/`      | Division       |

### Examples

**Addition:**
```bash
python calculator.py 10 + 5
# Result: 15.0
```

**Subtraction:**
```bash
python calculator.py 20 - 8
# Result: 12.0
```

**Multiplication:**
```bash
python calculator.py 7 '*' 6
# Result: 42.0
```

> Note: The `*` operator may need to be quoted to prevent shell expansion.

**Division:**
```bash
python calculator.py 100 / 4
# Result: 25.0
```

### Error Handling

**Division by zero:**
```bash
python calculator.py 10 / 0
# Error: Division by zero
```

**Invalid operator:**
```bash
python calculator.py 10 % 5
# Error: Unsupported operator '%'
```

**Invalid input (non-numeric values):**
```bash
python calculator.py abc + 5
# Error: Invalid input
```

**Missing arguments:**
```bash
python calculator.py 10 +
# Error: Invalid input
```

## Running Tests

Run the full test suite using Python's unittest module:

```bash
python -m unittest discover tests
```

To run with verbose output:

```bash
python -m unittest discover tests -v
```

To run a specific test file:

```bash
python -m unittest tests.test_calculator
python -m unittest tests.test_operations
python -m unittest tests.test_parser
```
