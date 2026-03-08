# the function in this file uses the back substitution method to calculate the solution of ax = b
from lower_triangular import lower_tri
from matrix_transpose import transpose
import numpy as np
def back_sub(a, b):
    b_dummy = b
    low_a = lower_tri(a)
    x = np.zeros((a.shape[0], 1))
    x[0][0] = b[0][0]
    for i in range(1, a.shape[0]):
        for j in range(i):
            b_dummy[i][0] = b_dummy[i][0] - a[i][j]*