#!/usr/bin/python3
"""
This module contains code for rotating a n x n matrix
"""


def create_empty_matrix(n):
    """
    Returns an empty n x n matrix
    """
    empty_matrix = [[0 for _ in range(n)] for _ in range(n)]
    return empty_matrix


def rotate_2d_matrix(matrix):
    """
    Rotates the matrix provided as an argument
    """
    new_mat = create_empty_matrix(len(matrix))
    n = len(matrix)

    for i in range(n):
        for j in range(n, 0, -1):
            new_mat[i][n-j] = matrix[j-1][i]

    for i in range(n):
        matrix[i] = new_mat[i]
