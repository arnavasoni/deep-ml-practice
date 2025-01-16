# Single neuron
import math
def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    
    probabilities = []

    # single neuron
    for feature_vector in features:
        # calculate z
        z = sum(weight * feature for weight, feature in zip(weights, feature_vector)) + bias

        # calculate probability, and use sigmoid, cuz binary classification
        prob = 1 / (1 + math.exp(-z))
        probabilities.append(round(prob, 4))
    
    # mean square error
    mse = sum((prob - label) ** 2 for prob, label in zip(probabilities, labels)) / len(labels)
    mse = round(mse, 4)

    return probabilities, mse
 
features = [[0.5,1.0],
            [-1.5, -2.0],
            [2.0, 1.5]]

labels = [0, 1, 0]
weights = [0.7, -0.4]
bias = -0.1

probabilities, mse = single_neuron_model(features, labels, weights, bias)
print(probabilities, mse)
