#!/usr/bin/python3
"""8-rectangle.py module"""


class BaseGeometry():
    """class defined as BaseGeometry"""
    def area(self):
        """raises exception when area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """class Rectangle inherited from class BaseGeometry"""
    def __init__(self, width, height):
        """initializes class Rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
