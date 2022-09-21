#!/usr/bin/python3
"""5-save_to_json_file.py"""


import json


def save_to_json_file(my_obj, filename):
    """writes an object to text file using JSON representation"""
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(json.dumps(my_obj))
        f.close
