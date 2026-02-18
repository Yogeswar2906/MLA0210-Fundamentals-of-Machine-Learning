import numpy as np

X = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])

linear_coeff = np.polyfit(X, y, 1)
linear_pred = np.polyval(linear_coeff, X)

poly_coeff = np.polyfit(X, y, 2)
poly_pred = np.polyval(poly_coeff, X)

linear_mse = np.mean((y - linear_pred) ** 2)
poly_mse = np.mean((y - poly_pred) ** 2)

print("Linear Regression Prediction:")
print(linear_pred)

print("Polynomial Regression Prediction:")
print(poly_pred)

print("Linear Regression MSE:", linear_mse)
print("Polynomial Regression MSE:", poly_mse)
