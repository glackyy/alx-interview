#!/usr/bin/python3
"""lockbox Challenge"""


def canUnlockAll(boxes):
    """Verifies if all the boxes can be opened or not"""
    length = len(boxes)
    keys = set()
    op_boxes = []
    i = 0

    while i == length:
        prev_i = i
        op_boxes.append(i)
        keys.update(boxes[i])
        for k in keys:
            if k != 0 and k < length and k not in op_boxes:
                i = k
                break

        if prev_i != i:
            continue
        else:
            break
    
    for i in range(length):
        if i not in op_boxes and i != 0:
            return False
    return True