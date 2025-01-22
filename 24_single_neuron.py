# Single neuron
import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	probabilities = [] # Results of different samples after each probability goes through sigmoid function
	z = 0
	for feature_vector in features:
		z = sum(weight * feature for weight, feature in zip(weights, feature_vector)) + bias
		prob = 1 / (1 + math.exp(-z))
		probabilities.append(round(prob, 4))

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