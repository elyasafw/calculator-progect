import math


def add(n1, n2):
    """Adds two numbers and returns the sum."""
    return n1 + n2


def func_sub(n1, n2):
    """Subtracts the second number from the first."""
    return n1 - n2


def multiply(n1, n2):
    """Multiplies two numbers."""
    return n1 * n2


def divide(n1, n2):
    """Divides the first number by the second. Includes zero division check."""
    if n2 == 0:
        return "Error: Cannot divide by zero!"
    return n1 / n2


def holding(n1, n2):
    """Calculates the first number to the power of the second."""
    return n1 ** n2


def root(n1, n2=2):
    """Calculates the n-th root of a number. Default is square root."""
    if n1 < 0 and n2 % 2 == 0:
        return "Error: Cannot calculate even root of a negative number!"
    return n1 ** (1/n2)


def absolute_value(n1):
    """Returns the absolute value of a number (distance from zero)."""
    return abs(n1)


def triangle_area(base, height):
    """Calculates triangle area using base and height."""
    if base <= 0 or height <= 0:
        return "Error: Dimensions must be positive!"
    return (base * height) / 2


def square_area(length, width):
    """Calculates square or rectangle area using length and width."""
    if length <= 0 or width <= 0:
        return "Error: Dimensions must be positive!"
    return length * width


def calculate_circle(radius):
    """Calculates the area of a circle using its radius."""
    if radius <= 0:
        return "Error: Radius must be positive!"
    return 3.14159 * (radius ** 2)