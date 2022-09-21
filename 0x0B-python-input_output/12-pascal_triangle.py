#!/usr/bin/python3
"""3-to_json_string.py module"""


import json


def to_json_string(my_obj):
    """returns JSON representation of object"""
    return json.dumps(my_obj)
