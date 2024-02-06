#!/usr/bin/python3

import json

"""
Convert from JSON to sting.

No exceptions are handled.
"""

def to_json_string(my_obj):
    """Juts dump the object"""

    return json.dumps(my_obj)

