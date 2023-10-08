"""Will create a Pokemon from an API call to https://pokeapi.co website"""

import requests
from random import randint

from .pokemon import Pokemon

API_URL = "https://pokeapi.co/api/v2/"
"""API endpoint, DO NOT CHANGE, only adapt parameters."""

GENERATION_IDS = {1: [1, 151], 2: [152, 251]}
"""Starting and ending IDs of a Pokemon Generation
ex: Bulbasaur/Mew (1/151), Chikorita/Celebi (152/251)
"""

class ApiCall:
    """Will be used to get Pokemon infos from the website."""

    @classmethod
    def get_infos(cls, pokemon_id):
        """Given a Pokemon ID, we return the server's answer in JSON format."""
        api_url = API_URL + f"pokemon/{pokemon_id}"
        response = requests.get(api_url)
        return response.json()


class PokemonCreation:
    """This will be the Class used to create a new Pokemon.
    
    We will not use the Pokemon module,
    which exists as a blueprint for 'what is a Pokemon'
    """

    def __init__(self, xth_generation):
        """A Pokemon will be created randomly in the gen. asked by user.
        
        GENERATION_IDS contains the first and last Pokemon's ID of a generation
        The game will then select a Pokemon's ID between the possible IDs
        """
        self.pokemon_id = randint(GENERATION_IDS[xth_generation][0], GENERATION_IDS[xth_generation][1])
        self.pokemon_infos = ApiCall.get_infos(self.pokemon_id)
    
    def pokemon_created(self) -> Pokemon:
        """This function parses the json answer form API
        and returns a Pokemon object
        """
        pokemon_name = self.pokemon_infos["name"]
        pokemon_type1 = self.pokemon_infos["types"][0]["type"]["name"]
        try:
            pokemon_type2 = self.pokemon_infos["types"][1]["type"]["name"]
        except IndexError:
            pokemon_type2 = ""
        print(pokemon_type1 + " " + pokemon_type2)
        pokemon_height = self.pokemon_infos["height"]
        pokemon_weight = self.pokemon_infos["weight"]
        
        new_pokemon = Pokemon(self.pokemon_id, pokemon_name, pokemon_height,
                              pokemon_weight, pokemon_type1, pokemon_type2)
        return new_pokemon