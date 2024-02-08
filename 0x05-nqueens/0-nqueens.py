#!/usr/bin/python3
"""N Queen Module"""
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)
    if n < 4:
        print('N must be at least 4')
        exit(1)
    
    solutions = []
    placed_q = []
    st = False
    r = 0
    ct = 0

    while r < n:
        gob = False
        while ct < n:
            s = True
            for cor in placed_q:
                col = cor[1]
                if (col == ct or col + (r-cor[0]) == ct or
                        col - (r-cor[0]) == ct):
                    s = False
                    break
            if not s:
                if ct == n -1:
                    gob = True
                    break
                ct += 1
                continue

            cords = [r, ct]
            placed_q.append(cords)
            if r == n - 1:
                solutions.append(placed_q[:])
                