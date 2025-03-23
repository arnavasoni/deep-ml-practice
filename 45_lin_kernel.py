import numpy as np

def kernel_function(x1, x2):
    total = 0
    if len(x1) == len(x2):
        for tup in zip(x1, x2):
            total += tup[0] * tup[1]
    
    return total