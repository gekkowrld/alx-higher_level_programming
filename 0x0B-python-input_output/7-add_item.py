#!/usr/bin/python3

"""
Add arguments to a list then save them in a file.

No exceptions/errors will be handled
"""

from sys import argv
import json


def add_item(filename, args):
    """Add items to a file"""
    save_to_json = __import__('5-save_to_json_file').save_to_json_file
    load_from_json = __import__('6-load_from_json_file').load_from_json_file
    data_to_be_saved = []
    try:
        data_to_be_saved = load_from_json(filename)
        data_to_be_saved[len(data_to_be_saved):] = args
    except FileNotFoundError:
        pass

    save_to_json(data_to_be_saved, filename)


if __name__ == "__main__":
    filename = "add_item.json"
    args = argv[1:]
    add_item(filename, args)
