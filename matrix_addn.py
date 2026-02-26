import numpy as np
# considering the matrix to be of size m*n

def add(matrix1, matrix2):
    if matrix1.shape != matrix2.shape:
        print("The matrices cannot be added as they are of different order. Please check the input given.\n")
        return None
    elif matrix1.shape == matrix2.shape:
        result = np.zeros(matrix1.shape)
        for i in range(matrix1.shape[0]):
            for j in range(matrix1.shape[1]):
                result[i][j] = matrix1[i][j] + matrix2[i][j]
        print("The result of the addition is : \n", result)
        return result
          