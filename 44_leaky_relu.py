def leaky_relu(z: float, alpha: float = 0.01) -> float|int:
    return z if z > 0 else z * alpha

print(leaky_relu(5), leaky_relu(-2))