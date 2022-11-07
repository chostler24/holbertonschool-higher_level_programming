#!/usr/bin/python3
"""
Script takes in a letter and sends a POST
request to URL with letter as parameter
"""
import requests
import sys


if __name__ == "__main__":
    URL = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]


