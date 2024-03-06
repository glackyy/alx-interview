#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Returning the perimeter of the island described
    in grid"""
    ct = 0
    gd_max = len(grid) - 1
    lt_max = len(grid[0]) - 1

    for lt_index, lt in enumerate(grid):
        for ld_index, ld in enumerate(lt):
            if ld == 1:
                if ld_index == 0:
                    ct += 1
                    if lt[ld_index + 1] == 0:
                        ct += 1
                elif ld_index == lt_max:
                    if lt[ld_index - 1] == 0:
                        ct += 1
