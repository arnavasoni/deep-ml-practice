"""
	Implements the SELU (Scaled Exponential Linear Unit) activation function.

	Args:
		x: Input value

	Returns:
		SELU activation value
"""
import math
def selu(x: float) -> float:
    alpha = 1.6732632423543772
    scale = 1.0507009873554804
    if x < 0:
        val = scale * alpha * (math.exp(x) - 1)
    else:
        val = scale * float(x)
    return round(val, 4)