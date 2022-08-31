#!/usr/bin/python3
from sys import argv

__name__ = "__main__"

if len(argv) == 1:
    print("{} arguments.".format(len(argv) - 1))
elif len(argv) == 2:
    print("{} argument:".format(len(argv) - 1))
else:
    print("{} arguments:".format(len(argv) - 1))

for x in range(1, len(argv)):
    print("{}: {}".format(x, argv[x]))
