training_data = [
    (["Sunny", "Warm", "Normal", "Strong", "Warm", "Same"], "Yes"),
    (["Sunny", "Warm", "High", "Strong", "Warm", "Same"], "Yes"),
    (["Rainy", "Cold", "High", "Strong", "Warm", "Change"], "No"),
    (["Sunny", "Warm", "High", "Strong", "Cool", "Change"], "Yes")
]

hypothesis = [None] * len(training_data[0][0])

for attributes, label in training_data:
    if label == "Yes":
        if hypothesis[0] is None:
            hypothesis = attributes.copy()
        else:
            for i in range(len(attributes)):
                if hypothesis[i] != attributes[i]:
                    hypothesis[i] = "?"

print(hypothesis)
