#!/usr/bin/python3
"""
LockedBoxes
"""


def canUnlockAll(boxes):
    """ the solution function """
    if boxes is None or len(boxes) == 0:
        return False
    queue = [0]
    visited = set()
    while len(queue) > 0:
        box = queue.pop(0)
        if box not in visited:
            visited.add(box)
            for keyTo in boxes[box]:
                if keyTo < len(boxes):
                    queue.append(keyTo)
    return len(visited) == len(boxes)
