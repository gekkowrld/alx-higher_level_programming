#!/usr/bin/python

"""
Read data from a file.

No exceptions and error checking is done.
"""

def read_file(filename=""):
    """Read data and return the file data"""
    file_data = ''
    with open(filename, encoding='UTF-8') as f:
        file_data = f.read()

    print(f"{file_data}")
