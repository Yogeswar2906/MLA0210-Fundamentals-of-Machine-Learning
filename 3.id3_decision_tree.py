import math

data = [
    ["Sunny", "Hot", "High", "No"],
    ["Sunny", "Hot", "High", "No"],
    ["Overcast", "Hot", "High", "Yes"],
    ["Rain", "Mild", "High", "Yes"],
    ["Rain", "Cool", "Normal", "Yes"],
    ["Rain", "Cool", "Normal", "No"],
    ["Overcast", "Cool", "Normal", "Yes"],
    ["Sunny", "Mild", "High", "No"],
    ["Sunny", "Cool", "Normal", "Yes"],
    ["Rain", "Mild", "Normal", "Yes"]
]

attributes = ["Outlook", "Temperature", "Humidity"]

def entropy(labels):
    total = len(labels)
    return sum(
        -labels.count(c)/total * math.log2(labels.count(c)/total)
        for c in set(labels)
    )

def information_gain(data, index):
    total_entropy = entropy([row[-1] for row in data])
    values = set(row[index] for row in data)
    gain = total_entropy
    for v in values:
        subset = [row for row in data if row[index] == v]
        gain -= (len(subset)/len(data)) * entropy([row[-1] for row in subset])
    return gain

gains = [information_gain(data, i) for i in range(len(attributes))]
best_attribute = attributes[gains.index(max(gains))]

print("Best attribute selected by ID3:")
print(best_attribute)

sample = ["Sunny", "Cool", "High"]

if best_attribute == "Outlook":
    result = "No" if sample[0] == "Sunny" else "Yes"
else:
    result = "Yes"

print("New Sample:", sample)
print("Classification:", result)
