#!/usr/bin/python3
for digone in range(0, 10):
    for digtwo in range(digone + 1, 10):
        if digone == 8 and digtwo == 9:
            print("{}{}".format(digone, digtwo))
        else:
            print("{}{}".format(digone, digtwo), end=", ")
