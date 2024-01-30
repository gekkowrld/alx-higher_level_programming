#!/usr/bin/python3

"""
A program used to add two programs together.

Only int and floats values are accepted.\
        Any other value is not allowed.
        If other values are included, then
        raise a TypeError.
"""

def add_integer(a, b=98):
    """Add two values together

    The values to be accepted should be either float or int.
    """
    try:
        a = int(a)
    except (TypeError, ValueError, OverflowError):
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except (TypeError, ValueError, OverflowError):
        raise TypeError("b must be an integer")

    return a + b
