# Row / Column Mean
import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    matrix = np.array(matrix)
    res = []
    if mode == 'column':
        res = np.mean(matrix, axis = 0)
    
    if mode == 'row':
        res = np.mean(matrix, axis = 1)
    
    return res.tolist()

matrix = [[1, 3, 5],
          [2, 4, 6]]

print(calculate_matrix_mean(matrix, "column"))