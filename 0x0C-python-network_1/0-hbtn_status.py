#!/usr/bin/python3
"""Script that fetches a URL"""
import urllib.request


if __name__ == "__main__":
    r = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(r) as response:
        page = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(page)))
        print('\t- content: {}'.format(page))
        print('\t- utf8 content: {}'.format(page.decode('utf8')))
