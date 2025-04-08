import numpy as np

def jaccard_index(y_true, y_pred):
	# Write your code here
    intersect = np.array(y_true == y_pred).tolist()
    if True not in intersect:
        return 0.0
    i = intersect.index(True)
    count = 0
    while i < len(intersect):
        if intersect[i] == True:
            count +=1
        else:
            break
        i += 1
    result = count / len(y_pred)
    return round(result, 3)
