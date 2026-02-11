import numpy as np

X = np.array([[1, 20],
              [2, 21],
              [3, 22],
              [8, 30],
              [9, 31],
              [10, 32]])

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

def gaussian(x, mean, var):
    return np.exp(-(x - mean) ** 2 / (2 * var)) / np.sqrt(2 * np.pi * var)

predictions = []

for x in X:
    probs = []
    for i in range(len(classes)):
        likelihood = np.prod(gaussian(x, mean[i], var[i]))
        probs.append(prior[i] * likelihood)
    predictions.append(classes[np.argmax(probs)])

predictions = np.array(predictions)

confusion_matrix = np.zeros((2, 2), dtype=int)

for i in range(len(y)):
    confusion_matrix[y[i]][predictions[i]] += 1

accuracy = np.sum(y == predictions) / len(y)

print("Confusion Matrix:")
print(confusion_matrix)

print("Accuracy:")
print(accuracy)
