import math

data = [
    ['Low','Low','Good','High'],
    ['Medium','Medium','Good','Medium'],
    ['High','High','Poor','Low'],
    ['Medium','High','Average','Low']
]

attributes = ['Age','Mileage','Condition']

def entropy(data):
    labels = [row[-1] for row in data]
    total = len(labels)
    ent = 0
    for l in set(labels):
        p = labels.count(l)/total
        ent -= p * math.log2(p)
    return ent

def info_gain(data, index):
    total_entropy = entropy(data)
    values = set(row[index] for row in data)
    weighted_entropy = 0
    for v in values:
        subset = [row for row in data if row[index]==v]
        weighted_entropy += (len(subset)/len(data)) * entropy(subset)
    return total_entropy - weighted_entropy

gains = {attr:info_gain(data,i) for i,attr in enumerate(attributes)}
best_attr = max(gains, key=gains.get)

new_car = ['Medium','Low','Good']
prediction = 'High' if new_car[2]=='Good' else 'Low'

print("Information Gain:", gains)
print("Best Attribute:", best_attr)
print("Predicted Resale Value:", prediction)
