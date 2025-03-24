# Implement Compressed Row Sparse Matrix (CSR) Format Conversion

import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
    """
    Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

    :param dense_matrix: 2D list representing a dense matrix
    :return: A tuple containing (values array, column indices array, row pointer array)
    """
    vals = []
    col_idx = []
    row_ptr = [0]

    for row in dense_matrix:
        val_row = [ele for ele in row if ele != 0]
        idx_row = [i for i, ele in enumerate(row) if ele != 0]

        vals.extend(val_row)
        col_idx.extend(idx_row)

        # for each element in the row pointer array:
        # ele = no. of non-zero elements + total no. of non-zero elements existing before this
        row_ptr.append(row_ptr[-1] + len(val_row))

    return vals, col_idx, row_ptr