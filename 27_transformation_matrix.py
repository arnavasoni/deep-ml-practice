import numpy as np

def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	# Convert the lists to arrays
	C = np.array(C)
	B = np.array(B)

	# Find the inverse matrix of the desired basis
	C_inv = np.linalg.inv(C)

	# Dot product of inverse matrix & converting matrix
	P = np.dot(C_inv, B)
	return P