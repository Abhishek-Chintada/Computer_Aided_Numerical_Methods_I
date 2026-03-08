# Bug Fixer.
import time
from turtle import forward
import numpy as np
from det_gen import det
from adjoint_inverse import adjoint, inverse
from upper_triangular import upper_tri
from lower_triangular import lower_tri
from solution_inverse import sol_inv
from forwards import forward_sub
a = np.array([
    [ 0,  3, -1,  2],
    [ 4,  1,  0, -2],
    [-2,  4,  5,  1],
    [ 1, -1,  2, -3]
], dtype=float)
b = np.array([13, 0, 4, -12], dtype=float)
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
t0 =time.time()
sol = sol_inv(a, b)
t1 = time.time()
print(sol)
print("The time taken to calcualte the solution using the inverse method is ", (t1 - t0))
lu = np.array([[1, 8, 9], [4, 5, 6], [7, 2, 3]])
print(upper_tri(lu))
print(lower_tri(lu))
u = np.array([
    [ 2.0,  0.0,  0.0],
    [ 3.0, -1.0,  0.0],
    [-1.0,  2.0,  4.0]
])
b = np.array([4.0, 9.0, -4.0]).reshape(-1, 1)
x = forward_sub(u, b)
print(x)
