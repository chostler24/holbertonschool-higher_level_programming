#!/usr/bin/python3
"""6-load_from_json_file.py module"""


import json


def load_from_json_file(filename):
    """creates object from JSON file"""
    with open(filename, 'r') as f:
        return json.load(f)
