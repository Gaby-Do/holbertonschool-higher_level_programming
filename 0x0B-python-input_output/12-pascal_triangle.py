#!/usr/bin/python3
"""
12. Pascal's Triangle
Create a function def pascal_triangle(n): that returns a list of lists
of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Args:
        n: lenght of triangle side
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for row in range(1, n):
        row_aux = [1]
        row_ant = triangle[row - 1]
        for node in range(1, row):
            row_aux.append(row_ant[node] + row_ant[node - 1])
        row_aux.append(1)
        triangle.append(row_aux)
    return triangle
