import requests
import json

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

poke_data = response.json()
print(poke_data["name"].title())
print(poke_data["abilities"][0]["ability"]["name"])
print(poke_data["abilities"][1]["ability"]["name"])

print("=" * 50)

def fetch_pokemon_data(pokemon):
    '''Fetches data for a pokemon and returns a dictionary with the pokemon's name, abilities and weight.'''
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}")

    if response.status_code == 200:
        poke_data = response.json()

        poke_dict = {
            "name" :poke_data["name"].title(),
            "ability 1" :poke_data["abilities"][0]["ability"]["name"],
            "ability 2" :poke_data["abilities"][1]["ability"]["name"],
            "weight" :poke_data["weight"]
            }

        return(poke_dict)
    else:
        return "Bad response, try again!"

def calculate_average_weight():
    '''Fetches data for 3 pokemon and calculates the average weight of the 3 pokemon.'''
    pokemon_names = ["pikachu", "bulbasaur", "charmander"]
    poke1 = fetch_pokemon_data(pokemon_names[0])
    poke2 = fetch_pokemon_data(pokemon_names[1])
    poke3 = fetch_pokemon_data(pokemon_names[2])

    print(poke1)
    print(poke2)
    print(poke3)

    average_weight = (poke1["weight"] + poke2["weight"] + poke3["weight"]) / len(pokemon_names)

    print(f"The average weight of {poke1["name"]}, {poke2["name"]} and {poke3["name"]} is {average_weight}")

calculate_average_weight()