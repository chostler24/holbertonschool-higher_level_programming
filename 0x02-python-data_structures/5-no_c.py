#!/usr/bin/python3
def no_c(my_string):
    stringcopy = [x for x in my_string if x is not 'c' and x is not 'C']
    return ("".join(stringcopy))
