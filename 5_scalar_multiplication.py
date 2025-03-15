def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    # matrix = [[1, 2], [3, 4]], scalar = 2, result = [[2, 4], [6, 8]]
    res = [[ele * scalar for ele in row] for row in matrix]
    return res

matrix = [[1, 2], [3, 4]]
scalar = 2
print(scalar_multiply(matrix, scalar))