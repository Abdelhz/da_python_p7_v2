# da_python_p7_v2
# "Résolvez des problèmes en utilisant des algorithmes en Python"

# Déscription : les logiciels "Programme brute force" et "Programme optimisé" écris en Python, sont deux versions d'une application pour l'achat d'actions en bourse

# Création d'un environnement virtuel (env) pour le programme d'échecs  :

Nous devons tout d'abord créer un environnement virtuel python.

**NOTE :** Nous utilisons *python 3.9*

*Création d'un répertoir pour le projet :*

On ouvre d'abord un terminal (Si sous windows utiliser Git bash ou similaire pour les commandes unix)
Entrez la commande suivante :

> **mkdir knapsack_project**

*Copiez et coller toutes les source dans ce répertoire "knapsack_project"*
liste des sources:

**HADJ_ZOUBIR_ABDELWAHID_1_bruteforce_022022.py**

**HADJ_ZOUBIR_ABDELWAHID_2_optimized_022022.py**

**dataset1_Python_P7.csv**

**dataset2_Python_P7.csv**

**requirements.txt**


Création de l'env avec *venv*
Entrez les commandes suivantes une par une :

> **cd knapsack_project**

> **python -m venv env_knapsack_project**

A ce moment l'env est créé et il nous suffit de l'activer.

# Activer l'env :

Il faut pour cela naviguer dans le dossier *scrips* ou appelé "*bin*" sous linux, contenu dans le répertoir env_programme echecs;
Entrez les commandes suivantes une par une :

> **cd env_knapsack_project/scripts**

> **source activate**

L'env est maintenant activé.

# Installation des bibliothèques requises dans l'env :

*Revenir au répertoire du projet, "knapsack_project"*

Entrez la commande suivante :
> **cd ../..**

*Puis :*

> **pip install -r requirements.txt**

# Lancerment et execution du programme :

Pour ce projet nous avons deux programme à executer séparemment :
### Programme brute force :

Entrez la commande suivante :
> **python HADJ_ZOUBIR_ABDELWAHID_1_bruteforce_022022.py**

### Programme optimisé :
Pour cette partie nous avons deux ensembles test de données :

**dataset1_Python_P7.csv**

**dataset2_Python_P7.csv**

Pour tester le programme sur le 1er ensemble de donnée.

Entrez la commande suivante :

> **python HADJ_ZOUBIR_ABDELWAHID_2_optimized_022022.py dataset1_Python_P7.csv**

Pour tester le programme sur le 2eme ensemble de donnée.

Entrez la commande suivante :

> **python HADJ_ZOUBIR_ABDELWAHID_2_optimized_022022.py dataset1_Python_P7.csv**

### **Note :** Tous les résultats sont affichés sur la console du terminal


