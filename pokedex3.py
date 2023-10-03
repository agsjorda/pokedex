import requests
import sys


def search_pokemon(name):

    # response = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(name))
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
    pokemon = response.json()

    if response.status_code == 200:
        print(f"Name: {pokemon['name'].capitalize()}")
        print(f"HP: {pokemon['stats'][0]['base_stat']}")
        print("Abilities: ")
        for ability in pokemon['abilities']:
            print(f"{ability['ability']['name']}")

        if (pokemon['held_items']):
            print("Held Items:")
            for items in pokemon['held_items']:
                print(f"{items['item']['name']}")
        else:
            print("No Held Items")
    else:
        print(f"Pokemon {name} not found.")


if __name__ == "__main__":
    # Get up to 6 Pokémon names from command line arguments
    pokemon_names = sys.argv[1:7]

    for name in pokemon_names:
        search_pokemon(name)
        print()  # Add an empty line between each Pokémon's details
