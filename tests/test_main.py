import pytest
from calculator_main import compute_and_display

@pytest.mark.parametrize("num1_str, num2_str, operation_key, expected_output", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),  
    ("9", "3", 'unknown', "Unknown operation: unknown"),  
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),  
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.")  
])
def test_compute_and_display(num1_str, num2_str, operation_key, expected_output, capsys):
    compute_and_display(num1_str, num2_str, operation_key)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output