#!/usr/bin/python3
"""rectangle.py module"""
from models.base import Base
from re import X
from turtle import width


class Rectangle(Base):
    """class defining rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing rectangle"""
        super().__init__(id)

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        """placeholder for future comments"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    def area(self):
        """rectangle area"""
        return self.__width * self.__height

    def display(self):
        """print"""
        print(("\n" * self.__y) +
              "\n".join(((" " * self.__x) + ("#" * self.__width))
                        for i in range(self.__height)))

    def __str__(self):
        """string representation"""
        return "[{}] ({}) {}/{} - {}/{}".format(
            type(self).__name__, self.id, self.__x,
            self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """assigns argument to attribute"""
        i = 0
        for arg in args:
            i += 1
            if i == 1:
                self.id = arg
            if i == 2:
                self.__width = arg
            if i == 3:
                self.__height = arg
            if i == 4:
                self.__x = arg
            if i == 5:
                self.__y = arg

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            if key == "width":
                self.__width = value
            if key == "height":
                self.__height = value
            if key == "x":
                self.__x = value
            if key == "y":
                self.__y = value

    def to_dictionary(self):
        """returns dictionary representation"""
        return {
            "id": self.id, "width": self.__width,
            "height": self.__height, "x": self.__x,
            "y": self.__y
        }
