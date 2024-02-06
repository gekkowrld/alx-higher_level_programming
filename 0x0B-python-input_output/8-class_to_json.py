#!/usr/bin/python3

"""
Get JSON data and return a description and dats structure

No exceptions or errors are handled
"""


def class_to_json(obj):
    """Return the obj __dict__"""
    return obj.__dict__
