import requests
import sys


def search_pokemon(name):

    # response = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(name))
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
    pokemon = response.json()

    if response.status_code == 200:
        print(f"Name: {pokemon['name'].capitalize()}")
        print(f"ID: {pokemon['id']}")
        print(f"base experience: {pokemon['base_experience']}")
    else:
        print(f"Pokemon {name} not found.")


if __name__ == "__main__":
    search_pokemon(sys.argv[1])
