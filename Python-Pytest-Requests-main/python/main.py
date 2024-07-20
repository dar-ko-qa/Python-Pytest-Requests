import requests

URL = "https://api.pokemonbattle.ru/v2/"
TOKEN = "4b8891c81e7a28b6068ffb0e7e449974"
header = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_create = {
    "name": "generate",
    "photo_id": -1
}
body_put = {
    "pokemon_id": "32000",
    "name": "gimmighoul",
    "photo_id": 3
}
body_add_pokeball = {
    "pokemon_id": "32000"
}



# Создание покемона
response = requests.post(url = f'{URL}pokemons', headers = header, json = body_create)

print(response.json)


#Изменение покемона
response = requests.put(url = f'{URL}pokemons', headers = header, json = body_put)

print(response.json)


#поймать покемона в покебол
response = requests.post(url = f'{URL}trainers/add_pokeball', headers = header, json =  body_add_pokeball)

print(response.json)









