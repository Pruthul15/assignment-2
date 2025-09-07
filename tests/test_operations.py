import pytest
from app.operations import addition, subtraction, multiplication, division

def test_addition():
    assert addition(2.0, 3.0) == 5.0

def test_subtraction():
    assert subtraction(10.0, 4.0) == 6.0

def test_multiplication():
    assert multiplication(6.0, 7.0) == 42.0

def test_division_positive():
    assert division(9.0, 3.0) == 3.0

def test_division_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        division(9.0, 0.0)
