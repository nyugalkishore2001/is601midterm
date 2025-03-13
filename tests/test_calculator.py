'''Test File'''
from calculator import add,subtract,multiply,divide

def test_addition():
    '''Returns he sum of two numbers'''
    assert add(2,6) == 8

def test_subtraction():
    '''Test that subtraction function works '''    
    assert subtract(2,2) == 0

def test_multiplication():
    '''Test that multiplication function works '''    
    assert multiply(2,2) == 4

def test_division():
    '''Test that division function works '''    
    assert divide(2,2) == 1

def test_division_by_zero():
    '''Test that division function works '''    
    assert divide(2,0) == "Error: Cannot Divide by Zero"
    