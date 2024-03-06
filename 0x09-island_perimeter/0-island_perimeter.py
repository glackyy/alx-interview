#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Returning the perimeter of the island described
    in grid"""
    ct = 0
    gd_max = len(grid) - 1
    lt_max = len(grid[0]) - 1
    