#!/usr/bin/python3
"""
How to solve Lockboxes
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened.
Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """  a method that determines if all the boxes can be opened."""
    num_boxes = len(boxes)
    keys = [0]  # starting with the key of the first box
    visited = [False] * num_boxes  # to keep track of the boxes weve visited

    while keys:
        box = keys.pop()  # take a key from the list
        visited[box] = True  # mark the box as visited

        # looking inside of the current box for keys to other boxes
        for key in boxes[box]:
            if key < num_boxes and not visited[key]:
                keys.append(key)  # add new key to our list
    # checking if we visited all the box
    return all(visited)
