#!/usr/bin/python3

"""
Save an object to a file.

No error checking is done.
"""

import json

def save_to_json_file(my_obj, filename):
    """Save a json object in a file"""
    with open(filename,"w", encoding="UTF-8") as f:
        f.write(json.dumps(my_obj))

