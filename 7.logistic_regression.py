import numpy as np

X = np.array([[1],
              [2],
              [3],
              [8],
              [9],
              [10]])

y = np.array([0, 0, 0, 1, 1, 1])

X = np.hstack((np.ones((X.shape[0], 1)), X))

weights = np.zeros(X.shape[1])
lr = 0.01
epochs = 1000

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

for _ in range(epochs):
    z = np.dot(X, weights)
    predictions = sigmoid(z)
    gradient = np.dot(X.T, (predictions - y)) / len(y)
    weights -= lr * gradient

final_predictions = sigmoid(np.dot(X, weights))
final_predictions = np.where(final_predictions >= 0.5, 1, 0)

print("Predicted Output:")
print(final_predictions)

accuracy = np.sum(final_predictions == y) / len(y)
print("Accuracy:")
print(accuracy)
