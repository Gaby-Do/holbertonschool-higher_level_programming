#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for j in range(len(matrix)):
        for i in range(len(matrix[0])):
            if i < len(matrix[0]) - 1:
                print("{:d} ".format(matrix[j][i]), end='')
            else:
                print("{:d}".format(matrix[j][i]), end='')
        print()
