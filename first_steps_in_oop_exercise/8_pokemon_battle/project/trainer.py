from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name=None):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon.name not in [x.name for x in self.pokemons]:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        for pos, name in enumerate(self.pokemons):
            if pokemon_name == name.name:
                del self.pokemons[pos]
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        text = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        for info in self.pokemons:
            text += f"- {info.pokemon_details()}\n"

        return text

#Test Code
pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
