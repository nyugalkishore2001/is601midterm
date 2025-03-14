from decimal import Decimal
import pytest
from calculator.calculatorConstructor import CalcConstructor
from calculator.calculatorOperation import add, subtract, multiply, divide

def test_operation_add():
    calculation = CalcConstructor(Decimal('10'), Decimal('5'), add)
    assert calculation.perform() == Decimal('15')

def test_operation_subtract():
    calculation = CalcConstructor(Decimal('10'), Decimal('5'), subtract)
    assert calculation.perform() == Decimal('5')

def test_operation_multiply():
    calculation = CalcConstructor(Decimal('10'), Decimal('5'), multiply)
    assert calculation.perform() == Decimal('50')

def test_operation_divide():
    calculation = CalcConstructor(Decimal('10'), Decimal('5'), divide)
    assert calculation.perform() == Decimal('2')

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = CalcConstructor(Decimal('10'), Decimal('0'), divide)
        calculation.perform()