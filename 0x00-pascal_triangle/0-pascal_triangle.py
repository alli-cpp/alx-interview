#!/usr/bin/python3

"""
0-pascal_triangle.py: pascal_triangle()

"""



def pascal_triangle(n):
     """
        returns a lis of lists of integers
        Args:
            n (int): number of lists and digits
        Returns: list of lists
    """
    pascal = []
    if n <= 0:
        return pascal

    for i in range(n):
        inner = []
        for j in range(i + 1):
            if j == 0 or j == i:
                inner.append(1)
                continue
            top_inner = pascal[i - 1]
            value = top_inner[j - 1] + top_inner[j]
            inner.append(value)

        pascal.append(inner)

    return pascal
