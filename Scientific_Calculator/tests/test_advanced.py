from Scientific_Calculator.advanced_operations import (
    square_root,
    cube_root,
    log_base10,
    factorial,
    sin_deg
)
import math


def test_square_root():
    assert square_root(16) == 4


def test_cube_root():
    assert cube_root(27) == 3


def test_log_base10():
    assert log_base10(100) == 2


def test_factorial():
    assert factorial(5) == 120


def test_sin_deg():
    assert round(sin_deg(90), 5) == 1
