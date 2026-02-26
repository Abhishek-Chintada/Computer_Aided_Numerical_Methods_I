# this file is intended to reduce the syntax for finding the determinant of any square or augmented matrix.
from det_u_l import det_ul
from upper_triangular import upper_tri
def det(matrix):
    matrix = matrix.astype(float)
    up_tri, swap_count = upper_tri(matrix)
    return det_ul(up_tri, swap_count)