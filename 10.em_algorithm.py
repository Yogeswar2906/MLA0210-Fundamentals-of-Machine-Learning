import numpy as np

data = np.array([5, 9, 8, 4, 7])
iterations = 10

theta1 = 0.6
theta2 = 0.5

for _ in range(iterations):
    w1 = []
    w2 = []

    for x in data:
        p1 = theta1 ** x * (1 - theta1) ** (10 - x)
        p2 = theta2 ** x * (1 - theta2) ** (10 - x)
        total = p1 + p2
        w1.append(p1 / total)
        w2.append(p2 / total)

    w1 = np.array(w1)
    w2 = np.array(w2)

    theta1 = np.sum(w1 * data) / (10 * np.sum(w1))
    theta2 = np.sum(w2 * data) / (10 * np.sum(w2))

print("Estimated Parameters:")
print("Theta 1:", round(theta1, 3))
print("Theta 2:", round(theta2, 3))
