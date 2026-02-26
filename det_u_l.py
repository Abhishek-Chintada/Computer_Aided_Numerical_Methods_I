# this file is intended to fid the determinant of a matrix which is upper or lower triangular.
# here the matrix itself is an upper triangular matrix.
def det_ul(matrix, swap_count): # this function is written to handle the cases where sometimes the augmented matrix is sent as an argument.
    if matrix.shape[0] != matrix.shape[1]:
        print("Note : The following matrix is supposed to be augmented matrix and the last column is not cosidered for finding the determinant.")
        result = 1
        for i in range(matrix.shape[0]):
            result *= matrix[i][i]
        return (result*(-1)**swap_count)
    elif matrix.shape[0] == matrix.shape[1]:
        result = 1
        for i in range(matrix.shape[0]):
            result *= matrix[i][i]
        return (result*(-1)**swap_count)
    else:
        print("Error : Determinant cannot be found for this matrix.")
        return