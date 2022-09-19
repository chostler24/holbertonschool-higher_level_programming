#!/usr/bin/python3
"""0-read_file.py module"""


def read_file(filename=""):
    """Reads file and prints to stdout"""
    with open(filename, encoding="UTF-8") as i:
        x = i.read()
        print(x, end="")
