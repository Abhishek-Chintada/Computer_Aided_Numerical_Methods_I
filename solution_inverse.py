from adjoint_inverse import inverse
from matrix_mult import multiply

# this file contains the necessary code to find the solution using the inverse method.

def sol_inv(a, b):
    inv_a = inverse(a)
    solution_matrix = multiply(inv_a, b)
    return solution_matrix
    
# update - even though it is good enough for smaller matrices, it takes a heck lot of time for larger matrices.
# hence we get forth to the lu decomposition method.