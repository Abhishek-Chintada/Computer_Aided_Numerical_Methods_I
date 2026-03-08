import numpy as np
a = np.array([
    [ 4.0,  2.0,  0.0, 5.0],
    [ 2.0,  3.0,  1.0, 6.0],
    [-2.0,  1.0,  4.0, 9.0]
])
print(a.shape[0])
print(np.zeros((1, 2)))
x = a[1][0]
print(x)
for i in range(10):
    print(i)