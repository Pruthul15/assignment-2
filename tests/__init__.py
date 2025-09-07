import pytest
from app.operations import addition, subtraction, multiplication, division

def test_addition():
    assert addition(2, 3) == 5

def test_subtraction():
    assert subtraction(10, 4) == 6

def test_multiplication():
    assert multiplication(6, 7) == 42

def test_division_positive():
    assert division(9, 3) == 3

def test_division_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        division(9, 0)
