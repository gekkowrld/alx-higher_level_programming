#!/usr/bin/python3

"""
Write to file and return
the number of characters written
"""


def write_file(filename="", text=""):
    """Write text and return the data written"""
    with open(filename, 'w', encoding="UTF-8") as f:
        return f.write(text)
