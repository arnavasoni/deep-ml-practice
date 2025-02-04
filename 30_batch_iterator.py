import numpy as np

def batch_iterator(X, y = None, batch_size = 64):
    batches = [] # List for the batches to be collected in
    for i in np.arange(0, X.shape[0], batch_size):
        start, end = i, min(i+batch_size, X.shape[0])
        if y is not None:
            batches.append([X[start : end], y[start: end]])
        else:
            batches.append(X[start : end])
    return batches

X = np.array([[1, 2], 
                [3, 4], 
                [5, 6], 
                [7, 8], 
                [9, 10]])
y = np.array([1, 2, 3, 4, 5])
batch_size = 2
print(batch_iterator(X, y, batch_size))