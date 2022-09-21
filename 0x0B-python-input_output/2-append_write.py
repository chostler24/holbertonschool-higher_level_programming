#!/usr/bin/python3
"""2-append_write.py module"""


def append_write(filename="", text=""):
    """appends text to file and return number of chars"""
    with open(filename, "a", encoding="UTF-8") as f:
        f.write("{}".format(text))
        f.close
    return (len(text))
