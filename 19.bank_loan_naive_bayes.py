import numpy as np

X = np.array([
    [25, 30000],
    [30, 40000],
    [35, 50000],
    [45, 70000],
    [50, 80000],
    [55, 90000]
])

y = np.array([0, 0, 0, 1, 1, 1])

classes = np.unique(y)

mean = []
var = []
prior = []

for c in classes:
    X_c = X[y == c]
    mean.append(X_c.mean(axis=0))
    var.append(X_c.var(axis=0))
    prior.append(len(X_c) / len(X))

mean = np.array(mean)
var = np.array(var)
prior = np.array(prior)

def gaussian(x, m, v):
    return np.exp(-(x - m) ** 2 / (2 * v)) / np.sqrt(2 * np.pi * v)

predictions = []

for x in X:
    probs = []
    for i in range(len(classes)):
        probs.append(prior[i] * np.prod(gaussian(x, mean[i], var[i])))
    predictions.append(classes[np.argmax(probs)])

predictions = np.array(predictions)

accuracy = np.sum(predictions == y) / len(y)

print("Actual Loan Status:")
print(y)

print("Predicted Loan Status:")
print(predictions)

print("Accuracy:")
print(accuracy)
