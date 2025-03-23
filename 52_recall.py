import numpy as np
def recall(y_true, y_pred):
	tp = np.sum((y_true == 1) & (y_pred == 1))
	fn = np.sum((y_true == 1) & (y_pred == 0))
	# print((y_true == 1) & (y_pred == 1)): [ True False True False False True]
	if (tp + fn == 0):
		return 0
	else:
		return round(tp/(tp + fn), 3)