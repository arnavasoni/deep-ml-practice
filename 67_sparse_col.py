import numpy as np

# This is supposed to be the same as sparse row matrix; just transpose the matrix before.
def compressed_col_sparse_matrix(dense_matrix):
    dense_matrix = np.array(dense_matrix)
    
    dense_matrix_t = dense_matrix.T
    dense_matrix_t = dense_matrix_t.tolist()

    vals = []
    col_idx = []
    row_ptr = [0]

    for row in dense_matrix_t:
        val_row = [ele for ele in row if ele != 0]
        idx_row = [i for i, ele in enumerate(row) if ele != 0]

        vals.extend(val_row)
        col_idx.extend(idx_row)

        row_ptr.append(row_ptr[-1] + len(val_row))

    return vals, col_idx, row_ptr # so your col_idx is actually row_idx here & row_ptr is actually col_ptr