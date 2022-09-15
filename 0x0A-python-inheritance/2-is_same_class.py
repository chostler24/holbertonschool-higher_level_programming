#!/usr/bin/python3
"""2-is_same_class.py module"""


def is_same_class(obj, a_class):
    """
    returns true if object is exactly an instance
    of specified class, otherwise false
    """
    return (type(obj) == a_class)
