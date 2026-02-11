import math


# Roots and Powers
def square_root(x):
    if x < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(x)

def cube_root(x):
    return x ** (1/3)

def power(a, b):
    return a * b


# Logarithms
def log_base10(x):
    if x <= 0:
        raise ValueError("Log undefined for non-positive numbers")
    return math.log10(x)

def natural_log(x):
    if x <= 0:
        raise ValueError("Log undefined for non-positive numbers")
    return math.log(x)


# Trigonometry (radians)
def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)


# Trigonometry (degrees)
def sin_deg(x):
    return math.sin(math.radians(x))

def cos_deg(x):
    return math.cos(math.radians(x))

def tan_deg(x):
    return math.tan(math.radians(x))


# Factorial
def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if not isinstance(n, int):
        raise ValueError("Factorial only defined for integers")
    return math.factorial(n)


# Utility
def absolute(x):
    return abs(x)

def modulo(a, b):
    return a % b
import math


# Roots and Powers
def square_root(x):
    if x < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(x)

def cube_root(x):
    return x ** (1/3)

def power(a, b):
    return a ** b


# Logarithms
def log_base10(x):
    if x <= 0:
        raise ValueError("Log undefined for non-positive numbers")
    return math.log10(x)

def natural_log(x):
    if x <= 0:
        raise ValueError("Log undefined for non-positive numbers")
    return math.log(x)


# Trigonometry (radians)
def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)


# Trigonometry (degrees)
def sin_deg(x):
    return math.sin(math.radians(x))

def cos_deg(x):
    return math.cos(math.radians(x))

def tan_deg(x):
    return math.tan(math.radians(x))


# Factorial
def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if not isinstance(n, int):
        raise ValueError("Factorial only defined for integers")
    return math.factorial(n)


# Utility
def absolute(x):
    return abs(x)

def modulo(a, b):
    return a % b
