from decimal import Decimal
import pytest
from calculator.calculatorConstructor import CalcConstructor
from calculator.calculatorFunctions import CalcFunctions
from calculator.calculatorOperation import add, subtract

@pytest.fixture(autouse=True)  
def setup_calculations():
    CalcFunctions.clear_history()  
    CalcFunctions.add_calculation(CalcConstructor(Decimal('10'), Decimal('5'), add))
    CalcFunctions.add_calculation(CalcConstructor(Decimal('20'), Decimal('3'), subtract))

def test_add_calculation():
    calc = CalcConstructor(Decimal('2'), Decimal('2'), add)
    CalcFunctions.add_calculation(calc)
    assert CalcFunctions.get_latest() == calc

def test_get_history():
    history = CalcFunctions.get_history()
    assert len(history) == 2  

def test_clear_history():
    CalcFunctions.clear_history()
    assert len(CalcFunctions.get_history()) == 0  

def test_get_latest():
    latest = CalcFunctions.get_latest()
    assert latest.a == Decimal('20') and latest.b == Decimal('3')

def test_find_by_operation():
    add_operations = CalcFunctions.find_by_operation("add")
    assert len(add_operations) == 1  
    subtract_operations = CalcFunctions.find_by_operation("subtract")
    assert len(subtract_operations) == 1

def test_get_latest_with_empty_history():
    CalcFunctions.clear_history()  
    assert CalcFunctions.get_latest() is None