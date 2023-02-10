#!/usr/bin/python3
"""
Calculates the fewest number of operations needed to result
in exactly n H characters
"""


def minOperations(n):
    """
    Calculates the least number of operations
    needed to copy n H characters in the file.
    """
    if type(n) is not int or n <= 0:
        return 0
    number_of_operations = 0
    H = 1
    copy_all = 0
    paste = 0
    H_copied = 0
    while H < n:
        if n % H == 0:
            copy_all += 1
            H_copied = H
        paste += 1
        number_of_operations = copy_all + paste
        H += H_copied
    return number_of_operations
