#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_matrix.append([row[i] ** 2 for i in range(len(row))])
    return new_matrix
