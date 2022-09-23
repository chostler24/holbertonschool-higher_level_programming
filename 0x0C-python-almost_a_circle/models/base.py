#!/usr/bin/python3
"""base.py module"""
import json


class Base:
    """class defining Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """attributes"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string representation to file"""
        filename = cls.__name__ + '.json'
        dict_list = []
        if list_objs is not None:
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())

        with open(cls.__name__+".json", 'w', encoding='UTF-8') as f:
            f.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """returns list of JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            json.loads(json_string)
