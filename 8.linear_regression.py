import numpy as np

X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

mean_x = np.mean(X)
mean_y = np.mean(y)

numerator = np.sum((X - mean_x) * (y - mean_y))
denominator = np.sum((X - mean_x) ** 2)

b1 = numerator / denominator
b0 = mean_y - b1 * mean_x

y_pred = b0 + b1 * X

print("Intercept:", b0)
print("Slope:", b1)
print("Predicted Output:")
print(y_pred)
