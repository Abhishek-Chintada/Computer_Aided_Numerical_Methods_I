
# we are considering the matrix elementary row operations from now on.
# the first matrix row operation is to be the row interchange operation.
# we have to pass the index of the rows in the computer language so that we can use them to find out the elements in the row.
def ero1(matrix, row1, row2) : # row 1 is to be interchanged with the row2.
    for i in range(len(matrix[row1])):
        temp = matrix[row1][i]
        matrix[row1][i] = matrix[row2][i]
        matrix[row2][i] = temp

# the second elementary row operation is to multiply a row with a constant scalar.
# a simple snippet of code to make life easier in the long run.
def ero2(matrix, row, scalar):
     for i in range(len(matrix[row])):
         matrix[row][i] = matrix[row][i] * scalar
         
# the third elemetary row operation is to add a scalar multiple of one row to another row.
def ero3(matrix, row1, row2, scalar): # the row2 is multiplied by scalar and added to the row1.
    for i in range(len(matrix[row1])):
        matrix[row1][i] = matrix[row1][i] + matrix[row2][i] * scalar

def scalar_multiplication(matrix, scalar):
    matrix.astype(float)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j] * scalar
    return matrix