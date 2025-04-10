import numpy as np

def cosine_similarity(v1, v2):
	
    if v1.shape != v2.shape:
        raise ValueError("Vectors must be of the same shape")
    
    dot = np.dot(v1, v2)
    v1_mag = np.linalg.norm(v1)
    v2_mag = np.linalg.norm(v2)

    if v1_mag == 0 or v2_mag == 0:
        raise ValueError("Vectors cannot have zero magnitude.")

    return round((dot/(v1_mag * v2_mag)), 3)