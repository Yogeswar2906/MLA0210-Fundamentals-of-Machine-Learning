import math

X = [
    [1,1,3],
    [2,2,3],
    [3,3,1],
    [2,3,2]
]

y = ['High','Medium','Low','Low']

new_car = [2,1,3]

distances = []
for i in range(len(X)):
    d = math.sqrt(sum((X[i][j]-new_car[j])**2 for j in range(3)))
    distances.append((d,y[i]))

distances.sort()
k = 3
neighbors = distances[:k]

votes = {}
for _,label in neighbors:
    votes[label] = votes.get(label,0)+1

prediction = max(votes, key=votes.get)

print("Nearest Neighbors:", neighbors)
print("Predicted Resale Value:", prediction)
