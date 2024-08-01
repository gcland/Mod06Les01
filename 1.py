import requests
import json

#Task 1-2

# api_url = 'https://pokeapi.co/api/v2/pokemon/pikachu'
# response = requests.get(api_url)
# json_data = response.text

# pokemon = json.loads(json_data)

# #Task 2:
# #-----------------------------------------------------------------------------------#
# name = (pokemon['name'])
# ability1 = pokemon['abilities'][0]['ability']['name']
# ability2 = pokemon['abilities'][1]['ability']['name']

# print(f'Pokemon name: {name}.\nAbility 1: {ability1}.\nAbility 2: {ability2}.')

#Task 3:

api_url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(api_url)
json_data = response.text
pokemon = json.loads(json_data)

pokemon_list = ['Charizard', 'Rattata', 'Venusaur']

def fetch_pokemon_data(pokemon_list):
    for name in pokemon_list:
        for key in pokemon['results']:
            if key['name'] == name.lower():
                print(f'\nPokemon name: {key['name']}')
                api_url_name = key['url']
                response_name = requests.get(api_url_name)
                json_data_name = response_name.text
                pokemon_name = json.loads(json_data_name)
                i=1
                for ability in pokemon_name['abilities']:
                    print(f'{name}: Ability {i}: {ability['ability']['name']}')
                    i+=1
                print(f'{name}: Weight: {pokemon_name['weight']}')

fetch_pokemon_data(pokemon_list)

def calculate_average_weight(pokemon_list):  
    print()
    weight_list = []  
    for name in pokemon_list:
        for key in pokemon['results']:
            if key['name'] == name.lower():
                print(f'\nPokemon name: {key['name']}')
                api_url_name = key['url']
                response_name = requests.get(api_url_name)
                json_data_name = response_name.text
                pokemon_name = json.loads(json_data_name)
                weight_list.append(pokemon_name['weight'])
                print(f'{name}: Weight: {pokemon_name['weight']}')

    average = sum(weight_list)/len(weight_list)
    print(f"Average weight of Pokemon: {average}.")

calculate_average_weight(pokemon_list)



# fetch_pokemon_data('charizard')





# api_url = 'https://pokeapi.co/api/v2/pokemon/6/'
# response = requests.get(api_url)
# json_data = response.text
# pokemon = json.loads(json_data)

# name = (pokemon['name'])
# ability1 = pokemon['abilities'][0]['ability']['name']
# ability2 = pokemon['abilities'][1]['ability']['name']