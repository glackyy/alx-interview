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
                    ct += 1

                else:
                    if lt[ld_index - 1] == 0:
                        ct += 1
                    if lt[ld_index + 1] == 0:
                        ct += 1

                if lt_index == 0:
                    ct += 1
                    if grid[lt_index + 1][ld_index] == 0:
                        ct += 1

                elif lt_index == gd_max:
                    if grid[lt_index - 1][ld_index] == 0:
                        ct += 1
                    ct += 1

                else:
                    if grid[lt_index - 1][ld_index] == 0:
                        ct += 1
                    if grid[lt_index + 1][ld_index] == 0:
                        ct += 1
    return ct        
