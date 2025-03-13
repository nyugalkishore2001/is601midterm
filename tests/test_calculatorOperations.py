'''My Calculator Test'''
from calculator.calculatorOperation import add,subtract,multiply,divide

def test_add():
    '''Test that add function works '''    
    assert add(2,2) == 4

def test_subtract():
    '''Test that subtract function works '''    
    assert subtract(2,2) == 0

def test_multiply():
    '''Test that multiply function works '''    
    assert multiply(2,2) == 4

def test_divide():
    '''Test that divide function works '''    
    assert divide(2,2) == 1

def test_divide_by_zero():
    '''Test that divide by zero function works '''    
    assert divide(2,0) == "Error: Cannot Divide by Zero"