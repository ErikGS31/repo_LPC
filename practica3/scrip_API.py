import requests
import json 
print("ahora veremos un poco de información sobre mi Pokemon favorito")
url1 = 'https://pokeapi.co/api/v2/pokemon/196/'
peticion1 = requests.get(url1)
poke = json.loads(peticion1.content)
print ("Pokémon: " , poke['name'])

print ("su numero en la pokedex es:" , poke['id'])

url2 = 'https://pokeapi.co/api/v2/egg-group/5/'
peticion2 = requests.get(url2)
ghuevo = json.loads(peticion2.content)
print ("grupo huevo al que pertenece:" , ghuevo['name'] )

url3 = 'https://pokeapi.co/api/v2/type/14/'
peticion3 = requests.get(url3)
tipo = json.loads(peticion3.content)
print ("es de tipo:" , tipo['name'] )

url4 = 'https://pokeapi.co/api/v2/pokemon-species/196/'
peticion4 = requests.get(url4)
datos = json.loads(peticion4.content)
print ("su ratio de captura es:" , datos['capture_rate'] )
print ("el Pokémon cuenta con diferencias de genero: " , datos['has_gender_differences'])
