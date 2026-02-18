import numpy as np

X = np.array([[1,2],
              [2,3],
              [3,4],
              [6,7],
              [7,8],
              [8,9]])

y = np.array([0, 0, 0, 1, 1, 1])

def knn_predict(X, y, test, k=3):
    distances = []
    for i in range(len(X)):
        d = np.sqrt(np.sum((X[i] - test) ** 2))
        distances.append((d, y[i]))
    distances.sort()
    labels = [label for _, label in distances[:k]]
    return max(set(labels), key=labels.count)

knn_preds = [knn_predict(X, y, x) for x in X]
knn_acc = np.sum(knn_preds == y) / len(y)

classes = np.unique(y)
mean = [X[y == c].mean(axis=0) for c in classes]
var = [X[y == c].var(axis=0) for c in classes]
prior = [np.sum(y == c) / len(y) for c in classes]

def gaussian(x, m, v):
    return np.exp(-(x - m) ** 2 / (2 * v)) / np.sqrt(2 * np.pi * v)

nb_preds = []
for x in X:
    probs = []
    for i in range(len(classes)):
        probs.append(prior[i] * np.prod(gaussian(x, mean[i], var[i])))
    nb_preds.append(classes[np.argmax(probs)])

nb_preds = np.array(nb_preds)
nb_acc = np.sum(nb_preds == y) / len(y)

X_bias = np.hstack((np.ones((X.shape[0],1)), X))
w = np.zeros(X_bias.shape[1])

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

for _ in range(1000):
    w -= 0.01 * (X_bias.T @ (sigmoid(X_bias @ w) - y)) / len(y)

lr_preds = np.where(sigmoid(X_bias @ w) >= 0.5, 1, 0)
lr_acc = np.sum(lr_preds == y) / len(y)

print("KNN Accuracy:", knn_acc)
print("Naive Bayes Accuracy:", nb_acc)
print("Logistic Regression Accuracy:", lr_acc)
