csv_data = """Sunny,Warm,Normal,Strong,Warm,Same,Yes
Sunny,Warm,High,Strong,Warm,Same,Yes
Rainy,Cold,High,Strong,Warm,Change,No
Sunny,Warm,High,Strong,Cool,Change,Yes"""

data = [row.split(",") for row in csv_data.split("\n")]

concepts = [row[:-1] for row in data]
target = [row[-1] for row in data]

S = ["Ø"] * len(concepts[0])
G = [["?"] * len(concepts[0])]

for i in range(len(concepts)):
    if target[i] == "Yes":
        for j in range(len(S)):
            if S[j] == "Ø":
                S[j] = concepts[i][j]
            elif S[j] != concepts[i][j]:
                S[j] = "?"
        G = [g for g in G if all(g[k] == "?" or g[k] == S[k] for k in range(len(S)))]
    else:
        temp = []
        for g in G:
            for j in range(len(concepts[i])):
                if g[j] == "?" and S[j] != concepts[i][j]:
                    h = g.copy()
                    h[j] = S[j]
                    temp.append(h)
        G = temp

print(S)
for g in G:
    print(g)