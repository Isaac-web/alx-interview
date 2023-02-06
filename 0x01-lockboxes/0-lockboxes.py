#!/usr/bin/python3
"""
This module contains the code on lockboxes.
"""


def canUnlockAll(boxes):
    """
    Returns a boolean indicating whether all boxes can be opned or not.
    """
    _boxes = [False for _ in boxes]
    _boxes[0] = True
    for box_index in range(len(boxes)):
        if _boxes[box_index] is True:
            for key in boxes[box_index]:
                if key >= 0 and key < len(boxes):
                    _boxes[key] = True

    for box_index in range(len(boxes)):
        if _boxes[box_index] is True:
            for key in boxes[box_index]:
                if key >= 0 and key < len(boxes):
                    _boxes[key] = True

    closed_boxes = [box for box in _boxes if not box]
    return not bool(len(closed_boxes))
