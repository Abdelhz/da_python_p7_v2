import pandas as pd

# action_1 = {"nom_action": "action_1", "cout": 20, "benefice": 5}
# action_2 = {"nom_action": "action_2", "cout": 30, "benefice": 10}
# action_3 = {"nom_action": "action_3", "cout": 50, "benefice": 15}
# action_4 = {"nom_action": "action_4", "cout": 70, "benefice": 20}
# action_5 = {"nom_action": "action_5", "cout": 60, "benefice": 17}
# action_6 = {"nom_action": "action_6", "cout": 80, "benefice": 25}
# action_7 = {"nom_action": "action_7", "cout": 22, "benefice": 7}
# action_8 = {"nom_action": "action_8", "cout": 26, "benefice": 11}
# action_9 = {"nom_action": "action_9", "cout": 48, "benefice": 13}
# action_10 = {"nom_action": "action_10", "cout": 34, "benefice": 27}
# action_11 = {"nom_action": "action_11", "cout": 42, "benefice": 17}
# action_12 = {"nom_action": "action_12", "cout": 110, "benefice": 9}
# action_13 = {"nom_action": "action_13", "cout": 38, "benefice": 23}
# action_14 = {"nom_action": "action_14", "cout": 14, "benefice": 1}
# action_15 = {"nom_action": "action_15", "cout": 18, "benefice": 3}
# action_16 = {"nom_action": "action_16", "cout": 8, "benefice": 8}
# action_17 = {"nom_action": "action_17", "cout": 4, "benefice": 12}
# action_18 = {"nom_action": "action_18", "cout": 10, "benefice": 14}
# action_19 = {"nom_action": "action_19", "cout": 24, "benefice": 21}
# action_20 = {"nom_action": "action_20", "cout": 114, "benefice": 18}

# list_action = [action_1, action_2, action_3, action_4, action_5, action_6, action_7, action_8, action_9, action_10,
# action_11, action_12, action_13, action_14, action_15, action_16, action_17, action_18, action_19, action_20]

actions_dataframe = pd.read_csv("dataset1_Python_P7.csv")
list_action = actions_dataframe.to_dict("records")

delet_list = []
for action in list_action:
    if action["price"] <= 0 or action["profit"] <= 0:
        delet_list.append(action)
    else:
        action["price"] = int(action["price"]*100)
        action["profit_euro"] = int((round((action["price"]/100) * action["profit"], 2))*100)
print(len(delet_list))

for del_action in delet_list:
    list_action.remove(del_action)
del(delet_list)
for action in list_action:
    print(action)

print(len(list_action))

N = len(list_action)
W = 500*100
dp_table = [[0 for w in range(W + 1)] for i in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, W + 1):
        dp_table[i][j] = max(dp_table[i - 1][j], list_action[i - 1]["profit_euro"] + dp_table[i - 1][j - list_action[i - 1]["price"]] if j >= list_action[i - 1]["price"] else 0)

print(dp_table[1][4060])
result = dp_table[N][W]
print(f"Resultat = {result}")
list_items = []
w = W
for i in range(N, 0, -1):
    if result <= 0:
        break

    if result == dp_table[i - 1][w]:
        continue
    else:
        list_items.append(i - 1)
        result = result - list_action[i - 1]["profit_euro"]
        w = int(w - list_action[i - 1]["price"])

print(list_items)
benef = 0
cost = 0
for i in list_items:
    benef = benef + list_action[i]["profit_euro"]
    cost = cost + (list_action[i]["price"]/100)

print("here is printed benef")
print(f"Bebefice = {benef/10000}")
print(f"Cout total = {cost}")
print("\n\n")

for i in list_items:
    print(list_action[i])

