import numpy as np

def bhattacharyya_distance(p: list[float], q: list[float]) -> float:
    # Your code here
    if len(p) != len(q) or len(p) == 0 or len(q) == 0:
        return float(0)
    
    prod = [x * y for (x, y) in zip(p, q)]
    prod_rt = np.sqrt(prod)
    bc = sum(prod_rt)

    return -np.log(bc)