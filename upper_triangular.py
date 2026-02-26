from ero import ero3, ero1
import numpy as np
# in this file we are bound to make a matrix upper triangular at any cost.
# Update : trying to introduce partial pivoitng.
# matrix.shape[0] represents the number of rows inside the matrix
# similarly the matrix.shape[1] represents the nubmer of columns inside the matrix. 
def upper_tri(matrix_original):
    swap_count = 0
    matrix = matrix_original.copy().astype(float)
    for k in range(matrix.shape[1]):
        offset = np.argmax(np.abs(matrix[k:matrix.shape[0], k]))
        row_max = k + offset
        if matrix[row_max, k] == 0:
            continue
        if row_max != k:
            ero1(matrix, k, row_max)
            swap_count = swap_count + 1
        for j in range(k+1, matrix.shape[0]):
            ero3(matrix, j, k, -matrix[j][k]/matrix[k][k])
    return matrix, swap_count