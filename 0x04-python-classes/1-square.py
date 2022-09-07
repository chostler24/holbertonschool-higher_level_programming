#!/usr/bin/python3

"""This class is a Square"""


class Square:
    """This class defines a square"""
    def __init__(self, size=0):
        """Attributes for the class"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
