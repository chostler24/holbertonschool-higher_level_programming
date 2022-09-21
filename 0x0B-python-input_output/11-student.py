#!/usr/bin/python3
"""11-student.py module"""


class Student:
    """class defining Student"""
    def __init__(self, first_name, last_name, age):
        """initializing Student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to JSON attributes"""
        if attrs != None:
            x = {}
            for key, value in vars(self).items():
                if key in attrs:
                    x[key] = value
            return x
        return vars(self)

    def reload_from_json(self, json):
        """reloading from JSON attributes"""
        for key, value in json.items():
            setattr(self, key, value)
