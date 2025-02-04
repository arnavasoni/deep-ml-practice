import math

def sigmoid(z: float) -> float:

	result = 1/(1 + math.exp(-z))
	# rounding result upto 4 decimals
	return round(result, 4)