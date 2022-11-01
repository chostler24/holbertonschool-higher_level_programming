#!/usr/bin/python3
"""
Script takes in URL, sends request to URL,
displays body of response.
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    status = r.status_code
    if status >= 400:
        print('Error code: {}'.format(status))
    else:
        print(r.text)
