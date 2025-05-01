import numpy as np

def calculate_contrast(img) -> int:
	"""
	Calculate the contrast of a grayscale image.
	Args:
		img (numpy.ndarray): 2D array representing a grayscale image with pixel values between 0 and 255.
	"""
	return np.max(img) - np.min(img) if (np.max(img) <=255 and np.min(img) >= 0) else  ValueError("Intensity out of range")

img = np.array([[0, 50], [200, 255]])

res = calculate_contrast(img)
print(res)