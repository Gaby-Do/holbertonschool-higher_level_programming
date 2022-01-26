#!/usr/bin/python3
"""
Function that divides all elements of a matrix
All elements must be integers or floats
Returns a new matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements in a matrix by div
    Args:
        matrix: matriz of int or float
        div: divisor, int or float, > 0
    """

    new_matrix = []
    msg_div = "matrix_divided() missing 1 required positional argument: 'div'"
    msg_m1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg_m2 = "Each row of the matrix must have the same size"
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not div:
        raise TypeError(msg_div)

    if type(matrix) is list:
        lenght_row = len(matrix[0])
        for row in matrix:
            """check if all rows are same lenght"""
            if len(row) != lenght_row:
                raise TypeError(msg_m2)
            """check if each row is a list"""
            if type(row) is not list:
                raise TypeError(msg_m1)
            """check if each element is an integer or float"""
            for element in row:
                if type(element) is not int and type(element) is not float:
                    raise TypeError(msg_m1)
            """divide each element, build new row and adds it to new matrix"""
            new_matrix.append(list(map(lambda x: round(x/div, 2), row)))
    else:
        raise TypeError(msg_m1)
    return new_matrix
