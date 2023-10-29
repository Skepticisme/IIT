import random
#Saisir un entier positif n < 21 puis generer aleatoirement un tuple nomm tupp de n entier qui varient entre 1 et 10, Repeter la saisie de n si la valeur donnee est erronee
n = int(input("Saisissez un entier positif n < 21 : "))
while n < 0 or n > 20:
    n = int(input("Erreur. Saisissez un entier positif n < 21 : "))

tupp = tuple(random.randint(1, 10) for _ in range(n))
print(tupp)

#Extraire  a partir de tupp un tuple nomme tupp_seg , qui contient m listes dont chacun comporte k chiffres ordonnes dans l'ordre decroissant 
m = random.randint(1, n)
k = random.randint(1, n)
tupp_seg = tuple(sorted(random.sample(tupp, k), reverse=True) for _ in range(m))
print(tupp_seg) 
#Ajouter a la premiere position de chaque list de tupp_seg une valeur representant la somme de ses elements
tupp_seg = tuple([sum(tupp_seg[i])] + list(tupp_seg[i]) for i in range(len(tupp_seg))) 
print(tupp_seg)
#Ecrirre en une seule instruction un programme permettant de transofmmer tupp_seg en une chaine de caractere nomme ch_nombre ou chaque nombre duplique n'apparait qu'une seule fois 
ch_nombre = " ".join(set(" ".join(str(number) for number in tupp_seg)))

 
    