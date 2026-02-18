import numpy as np

X = np.array([
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.0, 1.4, 0.2],
    [5.0, 3.4, 1.5, 0.2],
    [6.5, 3.0, 5.2, 2.0],
    [6.3, 2.9, 5.6, 1.8],
    [6.7, 3.1, 5.6, 2.4]
])

y = np.array([
    "Setosa",
    "Setosa",
    "Setosa",
    "Virginica",
    "Virginica",
    "Virginica"
])

classes = np.unique(y)

mean = {}
var = {}
prior = {}

for c in classes:
    X_c = X[y == c]
    mean[c] = X_c.mean(axis=0)
    var[c] = X_c.var(axis=0)
    prior[c] = len(X_c) / len(X)

def gaussian(x, mean, var):
    return np.exp(-(x - mean) ** 2 / (2 * var)) / np.sqrt(2 * np.pi * var)

def predict(sample):
    probs = {}
    for c in classes:
        likelihood = np.prod(gaussian(sample, mean[c], var[c]))
        probs[c] = prior[c] * likelihood
    return max(probs, key=probs.get)

test_sample = np.array([5.0, 3.5, 1.3, 0.3])

print("Test Sample:", test_sample)
print("Predicted Iris Class:", predict(test_sample))
