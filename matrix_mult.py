import numpy as np

# first we need to make sure that we are implementing the algorithm in the generic method and not use any functions from numpy library.
# note that the matrices are multiplied in the order of matrix1 * matrix2
def multiply(matrix1, matrix2):
    # Ensure matrix2 is at least 2D for consistent indexing
    if matrix2.ndim == 1:
        matrix2 = matrix2.reshape(-1, 1)

    if matrix1.shape[1] != matrix2.shape[0]:
        print("Matrix multiplication between the given matrices is not possible.\n")
        return None

    result = np.zeros((matrix1.shape[0], matrix2.shape[1]))
    for i in range(matrix1.shape[0]):
        for j in range(matrix2.shape[1]):
            for k in range(matrix1.shape[1]):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    print("The result of the matrix multiplication is : \n", result)
    return result
