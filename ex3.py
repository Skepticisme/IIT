def calculer_prix_ttc(prix_ht, categorie):
    taux_tva = {'A': 0.07, 'B': 0.20, 'C': 0.25}
    return prix_ht + (prix_ht * taux_tva[categorie])

total_ttc = 0.0

while True:
    try:
        nombre_produits = int(input("Saisissez le nombre de produits : "))
        total_ttc = 0.0
        
        for _ in range(nombre_produits):
            prix_ht = float(input("Saisissez le prix HT du produit : "))
            while True:
                categorie = input("Saisissez la catégorie du produit (A, B ou C) : ").upper()
                if categorie in ['A', 'B', 'C']:
                    break
                else:
                    print("Catégorie invalide. Veuillez saisir A, B ou C.")

            prix_ttc = calculer_prix_ttc(prix_ht, categorie)
            total_ttc += prix_ttc

        print(f"Le prix total TTC est : {total_ttc:.2f} TND")
        break

    except ValueError:
        print("Prix HT invalide. Veuillez saisir une valeur numérique.")
