
import numpy as np

def r_squared(y_true, y_pred):

    y_true_mean = np.mean(y_true)

    for yt, yp in zip(y_true, y_pred):
        ssr = np.sum((y_true - y_pred) ** 2)
        sst = np.sum((y_true - y_true_mean) ** 2)

    try:
        r2 = 1 - (ssr/sst)

        if np.isinf(r2):
            return 0
        return round(r2, 3)
    
    except ZeroDivisionError:
        return 0
        
