#!/usr/bin/python3
"""2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotating a 2d matrix 90° clockwise"""
    left, right = 0, len(matrix) -1
    while left < right:
        for i in range(right - left):
            top, bott = left, right
            topLeft = matrix[top][left + i]
            matrix[top][left + i] = matrix[bott - i][left]
            matrix[bott - i][left] = matrix[bott][right - i]
            matrix[bott][right - i] = matrix[top + i][right]
            matrix[top + i][right] = topLeft
        right -= 1
        left += 1