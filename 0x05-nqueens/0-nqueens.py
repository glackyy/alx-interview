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
                if ct == n - 1:
                    gob = True
                    break
                ct += 1
                continue

            cords = [r, ct]
            placed_q.append(cords)
            if r == n - 1:
                solutions.append(placed_q[:])
                for cor in placed_q:
                    if cor[1] < n - 1:
                        r = cor[0]
                        ct = cor[1]
                for i in range(n - r):
                    placed_q.pop()
                if r == n - 1 and ct == n - 1:
                    placed_q = []
                    st = True
                r -= 1
                ct += 1
            else:
                ct = 0
            break
        if st:
            break
        if gob:
            r -= 1
            while r >= 0:
                ct = placed_q[r][1] + 1
                del placed_q[r]
                if ct < n:
                    break
                r -= 1
            if r < 0:
                break
            continue
        r += 1

    for index, v in enumerate(solutions):
        if index == len(solutions) - 1:
            print(v, end='')
        else:
            print(v)
