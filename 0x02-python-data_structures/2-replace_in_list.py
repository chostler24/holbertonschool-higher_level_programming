#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if not my_list:
        return
    x = len(my_list) - 1
    while x > -1:
        print("{:d}".format(my_list[x]))
        x -= -1
