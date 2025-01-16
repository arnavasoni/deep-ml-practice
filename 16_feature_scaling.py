import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	# Required to perform standardization
	data_mean = np.mean(data, axis = 0)
	std = np.std(data, axis = 0)

	# Required for normalization
	min_val = np.min(data, axis = 0)
	max_val = np.max(data, axis = 0)

	standardized_data =  (data - data_mean) / std
	
	normalized_data = (data - min_val) / (max_val - min_val)
	return standardized_data.tolist(), normalized_data.tolist()

data = np.array([[1, 2], [3, 4], [5, 6]])

print(feature_scaling(data))