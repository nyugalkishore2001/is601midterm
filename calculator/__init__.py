from decimal import Decimal
from typing import Callable
from calculator.calculatorConstructor import CalcConstructor
from calculator.calculatorOperation import add, subtract, multiply, divide

class Calculator:

    @staticmethod
    def _perform_calculation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        calcConstructor = CalcConstructor(a, b, operation)
        
        # Import inside the function to avoid circular import
        from calculator.calculatorFunctions import CalcFunctions  
        
        CalcFunctions.add_calculation(calcConstructor)
        return calcConstructor.perform()
    
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_calculation(a, b, add)
    
    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_calculation(a, b, subtract)
    
    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_calculation(a, b, multiply)
    
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_calculation(a, b, divide)
    