import numpy as np

income = np.array([20000, 30000, 25000, 50000, 60000, 55000])
loan_amount = np.array([5000, 7000, 6000, 20000, 25000, 23000])
credit_score = np.array(["Low", "Low", "Low", "High", "High", "High"])

def classify(income, loan):
    if income >= 40000 and loan <= 20000:
        return "High"
    else:
        return "Low"

predicted = []

for i in range(len(income)):
    predicted.append(classify(income[i], loan_amount[i]))

print("Actual Credit Score:")
print(credit_score)

print("Predicted Credit Score:")
print(predicted)

accuracy = np.sum(credit_score == predicted) / len(credit_score)
print("Accuracy:")
print(accuracy)
