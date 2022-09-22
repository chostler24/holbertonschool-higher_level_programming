#!/usr/bin/python3
"""rectangle.py module"""
from models.base import Base


class Rectangle(Base):
    """class defining rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing rectangle"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        self.__y = y

    def __str__(self):
        """string representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """rectangle area"""
        return self.__width * self.__height
