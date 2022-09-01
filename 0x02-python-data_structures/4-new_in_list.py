#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listcopy = my_list.x()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.listcopy()
    else:
        listcopy[idx] = element
        return listcopy
