'''My Calculator Test'''
from calculator import Calculator

def test_add():
    '''Test that add function works '''    
    assert Calculator.add(2,2) == 4

def test_subtract():
    '''Test that subtract function works '''    
    assert Calculator.subtract(2,2) == 0

def test_multiply():
    '''Test that multiply function works '''    
    assert Calculator.multiply(2,2) == 4

def test_divide():
    '''Test that divide function works '''    
    assert Calculator.divide(2,2) == 1

def test_divide_by_zero():
    '''Test that divide by zero function works '''
    assert Calculator.divide(2,0) == "Error: Cannot Divide by Zero"