#!/usr/bin/python3
"""9-student.py"""


class Student:
    """class defining Student"""
    def __init__(self, first_name, last_name, age):
        """initializing Student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
