#!/usr/bin/python3
"""4-inherits_from.py module"""


def inherits_from(obj, a_class):
    """
    returns true is the object is a instance of a class
    that inherited from the specified class, otherwise false.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
