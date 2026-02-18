from collections import Counter

data = [
    ('Low','Low','Good','High'),
    ('Medium','Medium','Good','Medium'),
    ('High','High','Poor','Low'),
    ('Medium','High','Average','Low')
]

new_car = ('Medium','Low','Good')

labels = [row[3] for row in data]
label_count = Counter(labels)

def prob(attr, value, label):
    count = 0
    total = 0
    for row in data:
        if row[3]==label:
            total += 1
            if row[attr]==value:
                count += 1
    return count/total if total else 0

scores = {}
for label in label_count:
    p = label_count[label]/len(data)
    for i in range(3):
        p *= prob(i,new_car[i],label)
    scores[label] = p

prediction = max(scores, key=scores.get)

print("Probabilities:", scores)
print("Predicted Resale Value:", prediction)
