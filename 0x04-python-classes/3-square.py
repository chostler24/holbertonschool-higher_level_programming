#!/usr/bin/python3

"""Class: Square"""


class Square:
    """This class is defined as a Square"""
    def __init__(self, size=0):
        """Attributes for the class"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
