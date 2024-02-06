#!/usr/bin/python3

"""
Append to a file.

No checks should be done on the file.
"""


def append_write(filename="", text=""):
    """Append text to filename"""
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
