#!/usr/bin/python3
"""
0-pascal_triangle.py: pascal_triangle()

"""


def pascal_triangle(n):
    """This function returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        inner = []
        for j in range(i + 1):
            if j == 0 or j == i:
                inner.append(1)
                continue
            top_inner = triangle[i - 1]
            value = top_inner[j - 1] + top_inner[j]
            inner.append(value)

        triangle.append(inner)

    return triangle
