import itertools

action_1 = {"nom_action" : "action_1", "cout" :20 , "benefice" :5 }
action_2 = {"nom_action" : "action_2", "cout" :30 , "benefice" :10 }
action_3 = {"nom_action" : "action_3", "cout" :50 , "benefice" :15 }
action_4 = {"nom_action" : "action_4", "cout" :70 , "benefice" :20 }
action_5 = {"nom_action" : "action_5", "cout" :60 , "benefice" :17 }
action_6 = {"nom_action" : "action_6", "cout" :80 , "benefice" :25 }
action_7 = {"nom_action" : "action_7", "cout" :22 , "benefice" :7 }
action_8 = {"nom_action" : "action_8", "cout" :26 , "benefice" :11 }
action_9 = {"nom_action" : "action_9", "cout" :48 , "benefice" :13 }
action_10 = {"nom_action" : "action_10", "cout" :34 , "benefice" :27 }
action_11 = {"nom_action" : "action_11", "cout" :42 , "benefice" :17 }
action_12 = {"nom_action" : "action_12", "cout" :110 , "benefice" :9 }
action_13 = {"nom_action" : "action_13", "cout" :38 , "benefice" :23 }
action_14 = {"nom_action" : "action_14", "cout" :14 , "benefice" :1 }
action_15 = {"nom_action" : "action_15", "cout" :18 , "benefice" :3 }
action_16 = {"nom_action" : "action_16", "cout" :8 , "benefice" :8 }
action_17 = {"nom_action" : "action_17", "cout" :4 , "benefice" :12 }
action_18 = {"nom_action" : "action_18", "cout" :10 , "benefice" :14 }
action_19 = {"nom_action" : "action_19", "cout" :24 , "benefice" :21 }
action_20 = {"nom_action" : "action_20", "cout" :114 , "benefice" :18 }

list_action = [action_1, action_2, action_3, action_4, 
action_5, action_6, action_7, action_8, action_9, action_10, 
action_11, action_12, action_13, action_14, action_15, action_16, 
action_17, action_18, action_19, action_20]
for action in list_action:
    action["benefice_euro"] = (action["cout"]/100)*action["benefice"]

new_list_combinaisons = []

for i in range(1, len(list_action)+1):
    list_combinaisons = itertools.combinations(list_action, i)

    somme_cout = 0
    somme_benefice = 0
    for combi in list_combinaisons:
        new_combi = {"combinaisons" : []}
        total = {"somme_benefice" : 0, "somme_cout" : 0}
        sum_benef = 0
        sum_cout = 0
        for element in combi:
            sum_benef = sum_benef + element["benefice_euro"]
            sum_cout = sum_cout + element["cout"]
            #print(element)
            new_combi["combinaisons"].append(element)
        
        if (sum_cout <= 500):
            if (sum_benef > somme_benefice):
                somme_benefice = sum_benef
                total["somme_benefice"] = sum_benef
                total["somme_cout"] = sum_cout
                new_combi["total"] = total
                #print("NOUVEAU COMBI :\n")
                #print(new_combi)
                # print(new_combi["combinaisons"])
                # print(new_combi["total"]["somme_cout"])
                new_list_combinaisons.append(new_combi)
            else:
                pass
        else:
            pass

new_list_combinaisons_sorted = sorted(new_list_combinaisons, key=lambda combinaison: (combinaison["total"]["somme_cout"], combinaison["total"]["somme_benefice"]))
new_list_combinaisons_sorted.reverse()


print(f"\n\n\n{new_list_combinaisons_sorted[0]}")
print(len(new_list_combinaisons_sorted))