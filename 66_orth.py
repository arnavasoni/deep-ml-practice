import numpy as np

def orthogonal_projection(v, L):
    """
    Compute the orthogonal projection of vector v onto line L.

    :param v: The vector to be projected
    :param L: The line vector defining the direction of projection
    :return: List representing the projection of v onto L
    """

    # Convert to numpy array
    v = np.array(v)
    L = np.array(L)

    # Calculate the projection
    num = v @ L
    den = L @ L

    orth = (num / den) * L

    return orth
