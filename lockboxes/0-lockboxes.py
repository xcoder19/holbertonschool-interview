#!/usr/bin/python3

"""Lockboxes module."""


def pushkeys(box, keys):
    """Append keys from box to keys list and deduplicate."""
    for key in box:
        keys.append(key)
        keys = list(dict.fromkeys(keys))
    return keys


def canUnlockAll(boxes):
    """Determine if all boxes can be unlocked."""
    remaining_boxes = len(boxes) - 1
    locked_boxes_index = []
    keys = []
    keys = pushkeys(boxes[0], keys)
    for box_index in range(1, len(boxes)):
        if box_index in keys:
            remaining_boxes -= 1
            keys = pushkeys(boxes[box_index], keys)
        else:
            locked_boxes_index.append(box_index)

    for i in locked_boxes_index:
        if i in keys:
            remaining_boxes -= 1
            keys = pushkeys(boxes[i], keys)

    if remaining_boxes == 0:
        return True
    else:
        return False
