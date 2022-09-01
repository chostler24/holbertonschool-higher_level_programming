#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in matrix:
            print("{:d}".format(col), end=" " if col is not row[-1] else "")
    print()
