#!/usr/bin/python3
""" A program that returns a list of lists of
    integers representing the Pascals triangle of n """


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascals triangle of n
    """
    if n <= 0:
        return []

    pascal_triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j])
            row.append(1)
        pascal_triangle.append(row)

    return pascal_triangle
