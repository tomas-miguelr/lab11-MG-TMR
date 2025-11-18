"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    try:
        result = math.sqrt(a)
    except ValueError:
        print("The value of a must be >= 0.")
        return 0
    else:
        return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

# First example
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError()
    else:
        return a / b

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError()
    else:
        return math.log(a, b)

def exponent(a, b):
    return a**b


