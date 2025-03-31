import numpy as np

def calculate_brightness(img):
    try:
        img = np.array(img, dtype=np.float32)
        
        # Ensure the image is 2D (grayscale) or 3D (color)
        if img.ndim not in [2, 3]:
            return -1
        
        # Validate pixel values
        if np.max(img) > 255 or np.min(img) < 0:
            return -1
        
        # Calculate mean brightness
        return round(np.mean(img), 2)
    except Exception:
        return -1
