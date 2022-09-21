#!/usr/bin/python3
"""8-class_to_json.py"""


def class_to_json(obj):
    """returns dictionary description for JSON serialization of object"""
    return obj.__dict__
