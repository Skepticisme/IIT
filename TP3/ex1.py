#Etant donne  la liste des  location des voitures : 
from icecream import ic
location = [['100TR', '16/10/2023' , 'V001X','V003X','V004X' ],
            ['100RE','11/10/2023','V001X','V002X'],
            ['101KP','16/11/2023','V001X','V002X','V004X'],
            ['102DD','19/11/2023','V001X','V004X']
            ]
# Le dictionnaire voitures : 
voitures =  { 
                'V001X':'Kia-rio', 
                'V002X':'clio',
                'V003X':'208',
                'V004X':'BMW Gran',
                'V005X':'Golf5'
             }
#La liste location est constitues de listes chacune representant une reference une data de location et l identifiant ou les identifiants des voitures loues chaque location doit avoir une date unique c est a dire qu une seule location peut etre creee a la meme data
#Le dictionnaire voitures represente la base des voitures ou la cle correspond a lidentifiant de la voiture et la valeur correspond a sa marue 

#1_ Creer une fonction get_voiture id_voiture(id_voiture,v=voitures ) qui prend

""" 
get_voiture(id_voiture,v=voitures)
id_voiture :  Voiture ID, v = dictionary  
A function that search for the vehicule based on a provided ID and a dictionary that contains a list of vehicules, default is voitures,  if no vehicule corresponds to the ID then return false. 
""" 
def get_voiture(id_voiture  ,  v = voitures ): 
    vehiculeById = v[id_voiture] if id_voiture in v else False 
    return vehiculeById

print(get_voiture('V004X'))
print(get_voiture('1'))

"""
get_voitures(*id_voitures,v=voitures) 
*id_voitures is a tuple of IDs 
v a dictionary of vehicules (Keys are IDS values are Vehicule Names)
returns a list of dictionarys each has one key and one value 
"""



def get_voitures(*id_voitures,v=voitures): 
    keys = list(id_voitures)
    """ Change to use get_voiture later on"""
    values = [ get_voiture(elem) for elem in id_voitures ] 
    results = [{key:value} for key,value in zip(keys,values)]
    return results


print(get_voitures('V004X','V001X','V002X','V003X','V005X'))

"""
transformer_location(location ) 
location is a list  
it trasnforms location into a dictionary where each key corresponds to a date and each value is a  dictionary of vehicule id and vehicule name,rented on that date
"""
def transformer_location(location):
    return {elem[1]: {elem[i]: get_voiture(elem[i]) for i in range(2, len(elem))} for elem in location}

print(transformer_location(location))

"""
voiture_louees(loc=location)
returns a list of vehicles rented on a specific date 
"""
def voiture_louees(loc=location):
    all_rented_ids = [elem[2:] for elem in loc]
    #turn all_rented_ids into a list of ids 
    all_rented_ids = [id for elem in all_rented_ids for id in elem] 
    return list(set(all_rented_ids))
ic(voiture_louees()) 

"""
nombre_location(location)t,*v_louees) 
location_t is a dictionary  and v_louees is a list of rented vehicles in location_t 
returns a dictionary where each key is a rented vehicle and each value is the number of times it was rented 
independently of the date
"""
def nombre_location(location_t,*v_louees):
    return {vehicule: sum([1 for elem in location_t.values() for key in elem.keys() if key == vehicule]) for vehicule in v_louees}

ic(nombre_location(transformer_location(location),*voiture_louees()))



def liste_marques(n=2,**v):
    return [v[key] for key in v.keys() if v[key] >= n] if v else None

ic(liste_marques(**nombre_location(transformer_location(location),*voiture_louees())))

    

