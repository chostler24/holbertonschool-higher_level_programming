#!/usr/bin/python3
"""
Script
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    URL = 'https://api.github.com/user'
    user = sys.argv[1]
    tok = sys.argv[2]
    r = requests.get(URL, auth=HTTPBasicAuth(user, tok)).json()
    print(r.get("id"))
