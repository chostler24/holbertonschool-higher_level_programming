#!/usr/bin/python3
"""
Script takes in URL and email address, sends
POST request to URL with email as parameter,
displays body of response.
"""
import requests
import sys


if __name__ == "__main__":
    URL = sys.argv[1]
    val = {'email': sys.argv[2]}
    r = requests.post(URL, val)
    print(r.text)
