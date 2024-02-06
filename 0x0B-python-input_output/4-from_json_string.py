#!/usr/bin/python3

"""
Convert from JSON to to str (fr)

No exceptions are checked.
"""

import json

def from_json_string(my_str):
    """Return JSON"""
    return json.loads(my_str)

