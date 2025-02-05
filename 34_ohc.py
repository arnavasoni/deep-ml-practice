import numpy as np

def to_categorical(x, n_col=None):
	labels = np.unique(x).tolist() # gives the number of unique labels available.
	
	if len(labels) != n_col:
		labels = [i for i in range(labels[-1]+1)]
	res = np.zeros((x.shape[0], len(labels)))
	for i in range(x.shape[0]):
		res[i][x[i]] = 1
	return res
	
x = np.array([0, 1, 2, 1, 0])
output = to_categorical(x)
print(output)