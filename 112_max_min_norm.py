def min_max(x: list[int]) -> list[float]:
    if x is None or len(x) == 0:
        return []
    
    x_max = max(x)
    x_min = min(x)

    if x_max == x_min:
        return [float(0)] * len(x)
        
    norm_x = [(ele - x_min) / (x_max - x_min) for ele in x]

    return norm_x

print(min_max([1, 2, 3, 4, 5]))