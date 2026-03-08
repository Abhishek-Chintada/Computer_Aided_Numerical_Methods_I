# the function in this file uses the forward substitution method to calculate the solution of ax = b
from lower_triangular import lower_tri
import numpy as np
def forward_sub(a, b):
    b = b.astype(float)
    augmented = np.column_stack((a, b))
    low_a, _ = lower_tri(augmented)
    x = np.zeros((a.shape[0], 1))
    x[0] = low_a[0][a.shape[1]]/low_a[0][0]
    for i in range(1, low_a.shape[0]):
        for j in range(i):
            low_a[i][a.shape[1]] = low_a[i][a.shape[1]] - (low_a[i][j]*x[j][0])
        x[i] = low_a[i][a.shape[1]]/low_a[i][i]
    return x