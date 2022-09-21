#!/usr/bin/python3
"""1-write_file.py module"""


def write_file(filename="", text=""):
    """writes string to text file and returns number of chars"""
    with open(filename, 'w+') as f:
        return f.write(text)
