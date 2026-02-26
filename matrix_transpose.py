import numpy as np
# writing a function to find the transpose of a matrix
def transpose(matrix):
    result = np.zeros(matrix.shape)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            result[j][i] = matrix[i][j]
    print("The result of the matrix transpose is : \n", result)
    return result