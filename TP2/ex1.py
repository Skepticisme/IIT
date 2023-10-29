import re
mot = "Aap44193th23zyt889D3on    "
#Supprimer les espaces de bord de mot
mot = mot.strip();
print(mot)
#Afficher le nombre de lettres en majuscule dans mot
count = len(list(filter(lambda x: x.isupper(), mot)))
print(count)
#Afficher le nombre de caracteres non redondants dans mot
count = len(set(mot))
print(mot)
#Dans une seule ligne de code, remplaces les caracteres "A" ou 'a' de mote par '?', inverse la chaine et afficher la nouvelle chaine de caracteres obtenue  
mot = mot.replace("A", "?").replace("a", "?")[::-1]
print(mot)
#Remplacer les sous chaines composees de trois chiffres successifs dans mot par le symbole '@'
mot = re.sub(r"\d{3}", "@", mot)
print(mot)
#Calculer la somme des chiffres restants qui apparaissent dans mot
sum_digits = lambda mot: sum(int(char) for char in mot if char.isdigit())
print(sum_digits(mot))
#Verifier si mot est composable a partir de la chaine de caractere 'Ppython' La verificatoin ne doit pas etre sensible a la casse 
letters = "Ppython"
if all(char.lower() in letters.lower() for char in mot):
    print("Le mot est composable à partir de la chaîne de caractères 'Ppython'")
else:
    print("Le mot n'est pas composable à partir de la chaîne de caractères 'Ppython'")