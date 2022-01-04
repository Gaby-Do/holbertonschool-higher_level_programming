#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    #    new_matrix = [[x ** 2 for x in row] for row in matrix]
    #    return new_matrix
    # o de otro modo:
    new_matrix = []
    for row in matrix:
        new_list = list(map(lambda x: x * x, row))
        new_matrix.append(new_list)
    return new_matrix
