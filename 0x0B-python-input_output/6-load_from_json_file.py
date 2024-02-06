#!/usr/bin/python3

"""
Get JSON from a file

No Error checking is done.
"""

import json


def load_from_json_file(filename):
    """Load the data from specified file"""
    with open(filename, encoding="UTF-8") as f:
        return json.loads(f.read())
