import numpy as np
from det_gen import det
from ero import scalar_multiplication

def adjoint(matrix):  # adjoint is defined only for square matrices.
    matrix = matrix.copy().astype(float)
    m = matrix.shape[0]  # number of rows
    n = matrix.shape[1]  # number of columns # m = n;
    if m != n:
        print("The adjoint of the matrix cannot be found as the matrix is not square.")
        return None
    else:
        adj = np.zeros(
            (n, m)
        )  # the adjoint matrix is the transpose of the cofactor matrix.
        for i in range(m):
            for j in range(n):
                submatrix = np.delete(
                    np.delete(matrix, i, axis=0), j, axis=1
                )  # the row and column are deleted.
                cofactor = ((-1) ** (i + j)) * det(submatrix)
                adj[j, i] = cofactor
        return adj
        
def inverse(matrix) :
    matrix = matrix.copy().astype(float)
    determinant = det(matrix)
    if determinant == 0:
        print("The inverse of the matrix cannot be found as it is a singular matrix.\n")
        return
    else:
        adj = adjoint(matrix)
        assert determinant is not None
        print(1/determinant)
        inverse_matrix = scalar_multiplication(adj, 1/determinant)
        return inverse_matrix
    
    



