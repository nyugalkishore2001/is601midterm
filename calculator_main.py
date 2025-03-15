import sys
from calculator import Calculator
from decimal import Decimal, InvalidOperation
import logging
from calculator.logger import logger  

def compute_and_display(a, b, operation_name):
    """Perform a calculation and log the results."""
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        operation = operation_mappings.get(operation_name)

        if operation:
            result = operation(a_decimal, b_decimal)
            message = f"The result of {a} {operation_name} {b} is equal to {result}"
            print(message)
            logger.info(message)  
            error_message = f"Unknown operation: {operation_name}"
            print(error_message)
            logger.error(error_message)  

    except InvalidOperation:
        error_message = f"Invalid number input: {a} or {b} is not a valid number."
        print(error_message)
        logger.error(error_message)  
    except ZeroDivisionError:
        error_message = "Error: Division by zero."
        print(error_message)
        logger.error(error_message)  
    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(error_message)
        logger.exception(error_message)  

def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        logger.error("Invalid number of arguments provided.")
        sys.exit(1)
    
    _, a, b, operation = sys.argv
    compute_and_display(a, b, operation)

if __name__ == '__main__':
    main()