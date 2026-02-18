import numpy as np

X = np.array([
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.0, 1.4, 0.2],
    [6.2, 3.4, 5.4, 2.3],
    [5.9, 3.0, 5.1, 1.8],
    [5.5, 2.3, 4.0, 1.3],
    [6.5, 2.8, 4.6, 1.5]
])

y = np.array([
    "Setosa",
    "Setosa",
    "Virginica",
    "Virginica",
    "Versicolor",
    "Versicolor"
])

k = 3

def distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

def predict(test):
    d = []
    for i in range(len(X)):
        d.append((distance(test, X[i]), y[i]))
    d.sort()
    labels = [label for _, label in d[:k]]
    return max(set(labels), key=labels.count)

test_sample = np.array([5.8, 2.7, 5.1, 1.9])

print("Test Sample:", test_sample)
print("Predicted Iris Class:", predict(test_sample))
