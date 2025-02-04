import numpy as np

def shuffle_data(X, y, seed = None):
    if seed:
        np.random.seed(seed)
    
    idx = np.arange(X.shape[0]) # shuffling of indices
    np.random.shuffle(idx)
    return X[idx], y[idx]

X = np.array([[1, 2], 
                [3, 4], 
                [5, 6], 
                [7, 8]])
y = np.array([1, 2, 3, 4])

print(shuffle_data(X, y, 42))

'''
Shuffling the dataset helps avoid potential biases before training model

np.random.seed()
np.random.seed(0) makes the shuffles the numbers always in a certain way.

np.random.seed(num) will give the identical shuffling everytime.
'''