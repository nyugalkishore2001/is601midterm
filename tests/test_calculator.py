'''Test File'''
from calculator import add,subtract

def test_addition():
    '''Returns he sum of two numbers'''
    assert add(2,6) == 8

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(2,2) == 0
