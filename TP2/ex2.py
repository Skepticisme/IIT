""" 
Etant donne la chaine de caracteres ch suivante : 😀
"""
import random

ch="Python est est est populaire \n Python populaire est simple""" 
#Creer une liste nomme l_ch contenant des listes dont chacun comporte deux elements le premier represente un mot de cch et le deuxieme correspond a son nombre d'occuurence 
l_ch = [[word, ch.count(word)] for word in ch.split()]
print(l_ch)
#Melanger aleatoirement les elements de l_ch
random.shuffle(l_ch)
print(l_ch)

#Transformer les listes de format[mot,occurence] en des listes contenant mot repete occ fois l_ch = [['python','python'] , ['est','est','est']] etcetera 
l_ch = [[word] * count for word, count in l_ch]
#Transformer l_ch en une chaine de caractere nommee chT dont les mots sont separes par '*' 
chT = "*".join([" ".join(word) for word in l_ch])