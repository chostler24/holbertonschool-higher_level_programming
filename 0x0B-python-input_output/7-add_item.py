#!/usr/bin/python3
"""7-add_item.py module"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    json_make = load_from_json_file("add_item.json")
except:
    json_make = []

save_to_json_file(json_make + argv[1:], "add_item.json")
