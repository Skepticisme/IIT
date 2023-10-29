""" 
Etant donne le dictionnaire b_pharm qui contient les produits pharmaceutiques ou les noms sont utilises comme cles et les prix 
unitaires sont donnes en tant que valeurs corrspondantes
"""
b_pharm = { 'Doliprane':3.0,'Efferalgant':4.5,'orelox':9.25,'EcranFacial':35.9,'Paracetamol':11.8,'Atropine':22.5,'Augmentine':23.4,'GelNettoyant':15.5,'Thermometre':8.2,'SondeAspiration':12.5}
"""
Un Client peut commander un ou plusieirs medicaments Sa commmande est stockee dans une liste de dictionnaires nomme c_client. Chaque produit dans la commande est represnte par un dictionnaire ou la cle represente le nom du produit et la valeur
represente la quntite Dans cet exercice en supposant que c_client est defini comme suit : 
"""
c_client = [ {'Doliprane':1 } , {'GelNettoyant':2}, {'Dermosalic':1},{'Fervex':3} ]
#Transformer en une seule instruction c_cleint en un dictionnaire de la forme suivant {Doliprane':1,'GelNettoyant':2,'Dermosalic':1,'Fervex':3}
c_client = {key: value for d in c_client for key, value in d.items()}
#Creer et afficher un ensemble nomme prod_disp contenant les produits du client c_client qui sont disponnible dans la pharmacie b_pharm
prod_disp = (c_client.keys()) & b_pharm.keys()
print(prod_disp)
#Creer et afficher l'ensemble des prodiuts non disponnibles dans la commande du client, nomme produit_n_disp sans recourir a une structure iterative ou a une ecriture en comprehension
prod_n_disp = (c_client.keys()) - b_pharm.keys()
print(prod_n_disp)
#Traiter la commmande du client en transofmant c_client en une liste, l_cmd contenant un tuple de 2 elements pour chaque produit dans la commande. Le premier element represente le nom du produit commande et le deuxieme represente le prix total s'il est disponnible dans la pharmacie sinon il est defini comme None.
l_cmd = [(key, b_pharm[key] * value if key in b_pharm else None) for key, value in c_client.items()]
print(l_cmd)
#Determiner et afficher en une seule instruction le montant total de la commande du client c_client si le nombre de produits non disponibles dans la commande est superieur a 1 appliquer un reduction de 10% sur le montant total de la commande
total = sum(price for _, price in l_cmd if price is not None)
nones = sum(1 for _, price in l_cmd if price is None)
total *= 0.9 if nones > 1 else 1
print(total)