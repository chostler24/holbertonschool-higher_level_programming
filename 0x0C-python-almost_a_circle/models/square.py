#!/usr/bin/python3
"""square.py module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class defining Square inherited from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size

    def __str__(self):
        """string rep"""
        return "[{}] ({}) {}/{} - {}".format(
            type(self).__name__, self.id, self.x,
            self.y, self.width
        )

    def update(self, *args, **kwargs):
        """updating arguments"""
        i = 0
        for arg in args:
            i += 1
            if i == 1:
                self.id = arg
            if i == 2:
                self.width = arg
            if i == 3:
                self.x = arg
            if i == 4:
                self.y = arg

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            if key == "size":
                self.width = value
            if key == "x":
                self.x = value
            if key == "y":
                self.y = value
