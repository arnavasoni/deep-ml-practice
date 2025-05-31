import math
def elu(x: float, alpha = 1.0) -> float:
    """Compute the ELU activation function.
    
    Args:
        x (float): Input value
        alpha (float): ELU parameter for negative values (default 1.0)
    
    Returns:
        float: ELU activation value

    The ELU (Exponential Linear Unit) activation function is an
    advanced activation function that addresses some limitations of
    ReLU by providing negative values for negative inputs,
    which can help prevent the "dying ReLU" problem and speed up learning.
    """

    return float(x) if x > 0 else round((alpha * (math.exp(x) - 1)), 4)