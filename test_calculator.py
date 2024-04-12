
from calculator import Calculator

def test_addition():
    calc = Calculator()
    assert calc.addition(1,2)==3


def test_substraction():
    calc = Calculator()
    assert calc.substraction(6,2)==4


def test_division():
    calc = Calculator()
    assert calc.division(5,5)==1
