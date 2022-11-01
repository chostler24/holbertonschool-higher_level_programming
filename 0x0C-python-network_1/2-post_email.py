#!/usr/bin/python3
"""
Script takes a URL and email, sends a POST
request to passed URL with email as parameter,
displays body of response.
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    URL = sys.argv[1]
    val = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(val).encode('utf-8')
    r = urllib.request.Request(URL, data)
    with urllib.request.urlopen(r) as response:
        print(response.read().decode('utf-8'))
