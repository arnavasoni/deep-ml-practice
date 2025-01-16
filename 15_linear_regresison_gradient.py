import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    m, n = X.shape

    # weights = theta
    theta = np.zeros((n, 1))

    for _ in range(iterations):
        Z = X @ theta # Z = X*w + b, b = 0
        errors = Z - y.reshape(-1, 1) # loss
        updates = (X.T @ errors) / m # cost function
        # print(updates, updates.shape)
        theta -= alpha * updates # updates weights
    print(updates.shape)
    return np.round(theta.flatten(), 4)

X = np.array([[1, 1], [1, 2], [1, 3]])
y = np.array([1, 2, 3])
alpha = 0.01
iterations = 1000

print(linear_regression_gradient_descent(X, y, alpha, iterations))