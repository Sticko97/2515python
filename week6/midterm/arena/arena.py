import csv
from pokemon import Pokemon

class Arena:
    def __init__(self):
        self.pokemons =[]
        
    def add(self, pokemon:Pokemon):
        if not isinstance(pokemon, Pokemon):
            raise AttributeError("Invalid Pokemon")
        self.pokemons.append(pokemon)
        
    def active(self):
        active_pokemons = []
        for pokemon in self.pokemons:
            if pokemon.health > 0:
                active_pokemons.append(pokemon)
        return active_pokemons
        
    
    def __len__(self):
        return len(self.active())
    
    def load_from_file(self, file="pokemons.txt"):
        with open('pokemons.txt') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                health = int(row['health'])
                level = int(row['level'])
                pokemon = Pokemon(name)
                self.health = health
                self.level = level
                self.add(pokemon)
                


class Team:
    def __init__(self, level, active_pokemons):
        self.pokemons = []
        for pokemon in active_pokemons:
            if pokemon.level == level:
                self.pokemons.append(pokemon)

    def get_pokemons(self):
        return self.pokemons
