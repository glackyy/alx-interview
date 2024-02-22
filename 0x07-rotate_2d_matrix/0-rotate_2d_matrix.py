#!/usr/bin/python3
"""2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotating a 2d matrix 90° clockwise"""
    left, right = 0, len(matrix) -1
    while left < right:
        for i in range(right - left):
            top, bott = left, right