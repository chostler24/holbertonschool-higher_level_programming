#!/usr/bin/python3
"""3-is_kind_of_class.py"""


def is_kind_of_class(obj, a_class):
    """
    returns true if object is an instance of
    specified class or class that inherited
    from specified class, otherwise false
    """
    return isinstance(obj, a_class)
