#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for x, i in sorted(a_dictionary.items()):
        print(x, end="")
        print(":", i)
