from decimal import Decimal
from typing import Callable


class CalcConstructor:

    def __init__(self,a : Decimal,b : Decimal,operation : Callable[[Decimal,Decimal],Decimal]):
        self.a = a
        self.b = b
        self.operation = operation
    
    def create(a : Decimal, b : Decimal, operation : Callable[[Decimal,Decimal],Decimal]):
        return CalcConstructor(a,b,operation)
    
    def perform(self):
        if self.operation.__name__ == "divide" and self.b == Decimal('0'):
            raise ValueError("Cannot divide by zero")
        return self.operation(self.a, self.b)
    
    def __repr__(self):
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"