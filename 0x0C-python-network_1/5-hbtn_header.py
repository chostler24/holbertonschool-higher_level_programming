#!/usr/bin/python3
"""
Script takes in URL, sends request to URL
and displays value of variable X-Request-Id
in response header
"""
import requests
import sys


if __name__ == "__main__":
    print(requests.get(sys.argv[1]).headers.get('X-Request-Id'))
