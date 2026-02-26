import numpy as np

# first we need to make sure that we are implementing the algorithm in the generic method and not use any functions from numpy library.
# note that the matrices are multiplied in the order of matrix1 * matrix2
def multiply(matrix1, matrix2) :
     if matrix1.shape[1] != matrix2.shape[0] :
          print("Matrix mutiplication between the given matrices is not possible.\n")
          return None
     elif matrix1.shape[1] == matrix2.shape[0] :
         result = np.zeros((matrix1.shape[0], matrix2.shape[1]))
         for i in range(matrix1.shape[0]):
             for j in range(matrix2.shape[1]):
                 for k in range(matrix1.shape[1]) :
                     result[i][j] += matrix1[i][k] * matrix2[k][j]
         print("The result of the matrix multiplication is : \n", result)
         return result