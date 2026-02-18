import numpy as np

X = np.array([
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.0, 1.4, 0.2],
    [5.0, 3.4, 1.5, 0.2],
    [6.5, 3.0, 5.2, 2.0],
    [6.3, 2.9, 5.6, 1.8],
    [6.7, 3.1, 5.6, 2.4]
])

y = np.array([0, 0, 0, 1, 1, 1])

X = np.hstack((np.ones((X.shape[0], 1)), X))

w = np.zeros(X.shape[1])
lr = 0.1
epochs = 100

for _ in range(epochs):
    for i in range(len(X)):
        y_pred = 1 if np.dot(X[i], w) >= 0 else 0
        w += lr * (y[i] - y_pred) * X[i]

predictions = []
for i in range(len(X)):
    predictions.append(1 if np.dot(X[i], w) >= 0 else 0)

accuracy = np.sum(y == predictions) / len(y)

print("Predicted Classes:")
print(predictions)

print("Accuracy:")
print(accuracy)
