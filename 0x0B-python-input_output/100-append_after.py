#!/usr/bin/python3

"""
Search and update the after a certain specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Append after a string"""
    new_content = ""
    with open(filename, encoding="UTF-8") as f:
        for line_f in f:
            new_content += line_f
            if search_string in line_f:
                new_content += new_string

    with open(filename, "w", encoding="UTF-8") as fp:
        fp.write(new_content)
