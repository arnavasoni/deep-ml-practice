import numpy as np

# Precision: no. of predictions true that are actually true / number of predictions true, regardless if actually true or not.
 
def precision(y_true, y_pred):
    result, tp, fp = 0, 0, 0
    tp = sum((y_true == 1) & (y_pred == 1)) 
    fp = sum((y_true == 1) & (y_pred == 0)) 

    if (tp+fp) == 0:
        return 0
    
    result = tp / (tp + fp)
    return result