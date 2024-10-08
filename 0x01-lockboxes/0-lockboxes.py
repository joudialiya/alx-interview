#!/usr/bin/python3
"""
LockedBoxes
"""


def canUnlockAll(boxes):
    """ the solution function """
    if (type(boxes) is not list) or (boxes is None) or (len(boxes) == 0):
        return False
    queue = [0]
    visited = set()
    visited.add(0)
    while len(queue) > 0:
        box = queue.pop()

        for key in boxes[box]:
            if key < len(boxes) and key not in visited:
                visited.add(box)
                queue.append(key)
    return len(visited) == len(boxes)
