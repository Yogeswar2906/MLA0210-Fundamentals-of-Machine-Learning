import numpy as np

X = np.array([[2,4],
              [4,6],
              [4,4],
              [6,2],
              [6,4],
              [8,4]])

y = np.array(["A","A","A","B","B","B"])

k = 3

def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

def predict(test_point):
    distances = []
    for i in range(len(X)):
        dist = euclidean_distance(test_point, X[i])
        distances.append((dist, y[i]))
    distances.sort()
    neighbors = distances[:k]
    labels = [label for _, label in neighbors]
    return max(set(labels), key=labels.count)

test_point = np.array([5,5])

print("Test Point:", test_point)
print("Predicted Class:", predict(test_point))
