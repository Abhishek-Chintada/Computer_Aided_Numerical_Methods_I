# Bug Fixer.

import numpy as np
from det_gen import det
from adjoint_inverse import adjoint, inverse
from upper_triangular import upper_tri
a = np.array([
    [ 0,  3, -1,  2],
    [ 4,  1,  0, -2],
    [-2,  4,  5,  1],
    [ 1, -1,  2, -3]
], dtype=float)
print("This is the original matrix: \n")
print(a)
print("This is the upper triangular matrix: \n")
print(upper_tri(a))
print(f"This is the determinant of the matrix: {det(a)}\n")
print("This is the origial matrix after the determinant calculation: \n")
print(a)
print(f"This is the adjoint of the matrix: \n{adjoint(a)}\n")
print("This is the original matrix after the calcuation fo the adjoint matirx: \n")
print(a)
print(f"This is the inverse of the matrix: \n{inverse(a)}\n")
print("This is the original matrix after the calcuation of the inverse matrix: \n")
print(a)