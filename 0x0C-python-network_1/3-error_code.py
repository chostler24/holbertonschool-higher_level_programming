#!/usr/bin/python3
"""
Script takes in URL, sends request to URL and
displays body of response
"""
from asyncore import read
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    URL = sys.argv[1]
    r = urllib.request.Request(URL)
    try:
        with urllib.request.urlopen(r) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
