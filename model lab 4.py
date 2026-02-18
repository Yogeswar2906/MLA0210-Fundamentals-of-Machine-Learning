import math

X = [
    [1,1,3],
    [2,2,3],
    [3,3,1],
    [2,3,2]
]

y = [1,1,0,0]

weights = [0,0,0]
bias = 0
lr = 0.1
epochs = 1000

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

for _ in range(epochs):
    for i in range(len(X)):
        z = sum(X[i][j]*weights[j] for j in range(3)) + bias
        pred = sigmoid(z)
        error = y[i] - pred
        for j in range(3):
            weights[j] += lr * error * X[i][j]
        bias += lr * error

new_car = [2,1,3]
z = sum(new_car[j]*weights[j] for j in range(3)) + bias
prob = sigmoid(z)

prediction = "High" if prob >= 0.5 else "Low"

print("Probability:", prob)
print("Predicted Resale Value:", prediction)
