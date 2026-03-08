# the function in this file uses the back substitution method to calculate the solution of ax = b
from lower_triangular import lower_tri
import numpy as np
def forward_sub(a, b):
    b_dummy = b.copy().astype(float)
    low_a, _ = lower_tri(a)
    x = np.zeros((a.shape[0], 1))
    x[0] = b[0]/low_a[0][0]
    for i in range(1, low_a.shape[0]):
        for j in range(i):
            b_dummy[i] = b_dummy[i] - (low_a[i][j]*x[j][0])
        x[i] = b_dummy[i]/low_a[i][i]
    return x