import random


"""Documentation initiaition """
# Générer un nombre aléatoire entre 1 et 100
nombre_aleatoire = random.randint(1, 100)

# Initialiser le compteur de tentatives
tentatives = 0

print("Devinez le nombre entre 1 et 100.")

while True:
    # Demander à l'utilisateur de saisir un nombre
    saisie = input("Saisissez un nombre : ")
    
    # Vérifier si la saisie est un nombre entier
    if not saisie.isdigit():
        print("Veuillez saisir un nombre entier valide.")
        continue
    
    # Convertir la saisie en entier
    nombre_saisi = int(saisie)
    
    # Incrémenter le compteur de tentatives
    tentatives += 1
    
    if nombre_saisi < nombre_aleatoire:
        print("Le nombre est plus grand.")
    elif nombre_saisi > nombre_aleatoire:
        print("Le nombre est plus petit.")
    else:
        print(f"Bravo! Vous avez deviné le nombre {nombre_aleatoire} en {tentatives} tentatives.")
        break
