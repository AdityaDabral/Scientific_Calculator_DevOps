from Scientific_Calculator.basic_operations import add
from Scientific_Calculator.advanced_operations import (
    square_root,
    cube_root,
    log_base10,
    factorial,
    sin_deg,
    power
)
import math


def test_square_root():
    assert square_root(16) == 4

def test_power():
    assert power(2,8) == 256


def test_cube_root():
    assert cube_root(27) == 3


def test_log_base10():
    assert log_base10(100) == 2


def test_factorial():
    assert factorial(5) == 120


def test_sin_deg():
    assert round(sin_deg(90), 5) == 1

def test_integration_basic_and_advanced():
    # Step 1: Add two numbers
    result_add = add(3, 5)  # 8
    
    # Step 2: Raise result to power 2
    result_power = power(result_add, 2)  # 64
    
    # Step 3: Take square root
    final_result = square_root(result_power)  # 8
    
    # Final assertion
    assert final_result == 8
