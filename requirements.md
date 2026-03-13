Requirements

Overview
Build a simple Python CLI calculator that supports basic arithmetic operations.
The calculator should accept two numbers and an operator from the command line and print the result.

Goals
1. Accept user input from the command line.
2. Support addition, subtraction, multiplication, and division.
3. Handle divide-by-zero gracefully.
4. Include unit tests.

Functional Requirements
1. CLI Interface
The program must be invoked as:
python calculator.py <number1> <operator> <number2>
Example:
python calculator.py 10 + 5   -> Result: 15.0
python calculator.py 10 / 0   -> Error: Division by zero

2. Supported Operators
+ addition
- subtraction
* multiplication
/ division

3. Error Handling
If the operator is invalid, print: Error: Unsupported operator '<op>'
If dividing by zero, print: Error: Division by zero
If arguments are missing or not numbers, print: Error: Invalid input

4. Unit Tests
A file tests/test_calculator.py must cover:
- All four operations
- Division by zero
- Invalid operator
- Invalid input

Technical Requirements
Language: Python 3
No third-party dependencies (stdlib only)

Out of Scope
- GUI
- History/memory
- Floating point formatting
