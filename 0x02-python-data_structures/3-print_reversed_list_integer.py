#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    x = len(my_list) - 1

    while x > -1:
        print("{:d}".format(my_list[x]))
        x -= 1
