#!/usr/bin/python3
"""
Script that takes in a URL, sends request
to the URL, and displays value of X-Request-Id
variable in header of response.
"""
from urllib import request
import sys


if __name__ == "__main__":
    r = request.Request(sys.argv[1])
    with request.urlopen(r) as response:
        print(response.info()['X-Request-Id'])
