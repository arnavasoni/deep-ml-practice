import numpy as np
import statistics

def descriptive_statistics(data):
    mean = np.mean(data) # average
    median = np.median(data) # finding mid value after arranging discrete values in ascending order.
    mode = statistics.mode(data)
    variance = np.var(data)
    std_dev = variance**(0.5)
    # used numpy percentile below for quartiles
    percentiles = [np.percentile(data, 25), median, np.percentile(data, 75)]
    iqr = percentiles[2] - percentiles[0]
    stats_dict = {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": np.round(variance,4),
        "standard_deviation": np.round(std_dev,4),
        "25th_percentile": percentiles[0],
        "50th_percentile": percentiles[1],
        "75th_percentile": percentiles[2],
        "interquartile_range": iqr
    }
    return stats_dict