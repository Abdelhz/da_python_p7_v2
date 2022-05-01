import sys
import pandas as pd


def get_csv_data_to_item_list(dataset_name):
    """ Cette méthode génère une liste de dictionnaires à partir d'un fichier .csv """
    actions_dataframe = pd.read_csv(dataset_name)
    list_action = actions_dataframe.to_dict("records")
    return list_action


def clear_data(item_list):
    """ Cette méthode corrige et améliore les données obtenues à partir du fichier .csv"""
    list_to_delete = []
    for action in item_list:
        if action["price"] <= 0 or action["profit"] <= 0:
            list_to_delete.append(action)
        else:
            action["price"] = int(action["price"] * 100)
            action["profit_euro"] = int((round((action["price"] / 100) * action["profit"], 2)) * 100)

    for del_action in list_to_delete:
        item_list.remove(del_action)
    del list_to_delete
    return item_list


def knapsack_algo(item_list):
    """ Cette méthode contient l'algorithme KNAPSACk, qui pour un ensemble de taille N d'actions,
    sachant que chaque action possède une valeur Vi et un coût Wi et pour un coût maximal à ne pas dépasser W.
    l'algorithme KNAPSACK trouve la plus grande valeur V qui somme des valeurs de chaque action dans un ensemble
    d'actions dont la somme des coûts est inférieur ou égale à W.
    Sachant que chaque action ne peut être sélectionnée qu'une fois et d'une fraction d'action ne peut être prise. """
    dp_table = [[0 for w in range(W + 1)] for i in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, W + 1):
            dp_table[i][j] = max(dp_table[i - 1][j], item_list[i - 1]["profit_euro"] + dp_table[i - 1][
                j - item_list[i - 1]["price"]] if j >= item_list[i - 1]["price"] else 0)

    result = dp_table[N][W]
    return item_list, result, dp_table


def reverse_knapsack(result, dp_table, item_list):
    """ Cette méthode permet, avec la valeur obtenue avec la methode KNAPSACK de retrouver l'ensemble des actions
     utilisées pour obtenir cette valeur"""
    list_items = []
    w = W
    for i in range(N, 0, -1):
        if result <= 0:
            break

        if result == dp_table[i - 1][w]:
            continue
        else:
            list_items.append(i - 1)
            result = result - item_list[i - 1]["profit_euro"]
            w = int(w - item_list[i - 1]["price"])
    return list_items


filename = sys.argv[1]
list_action = get_csv_data_to_item_list(filename)
list_action = clear_data(list_action)
W = 500 * 100 # Coût maximal W = 500 "Contrainte de l'algorithme" multiplié par 100 pour le besoin de l'algorithme
N = len(list_action) # Taille des données "Le nombre d'actions à notre disposition"
list_action, result, dp_table = knapsack_algo(list_action)
list_items = reverse_knapsack(result, dp_table, list_action)

benef = 0
cost = 0
list_action_select = []
for i in list_items:
    list_action[i]["profit_euro"] = round(list_action[i]["profit_euro"] / 10000, 2) # Calcule du benefice obtenue
    # en euro pour chaque action
    list_action[i]["price"] = round(list_action[i]["price"] / 100, 2)
    list_action_select.append(list_action[i])
    benef = benef + list_action[i]["profit_euro"]
    benef = round(benef, 2)
    cost = cost + list_action[i]["price"]
    cost = round(cost, 2)


print(f"Benefice total = {benef}")
print(f"Coût total = {cost}")
print("\n\n")

print("Les actions selectionnées :\n")
for action in list_action_select:
    print(action)
