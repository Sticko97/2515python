import random
import csv
import json
import pytest


class Pokemon:
    """I READ THE TESTS AND INSTRUCTIONS
    
    consider pokemon type advantage into the pokemon class.
    in the fight method, pokemon may deal super effective damage and vice versa
    """
    def __init__(self, name, element):
        self.name = name
        element_list = ["water","fire","grass","electric"]
        if element not in element_list:
            raise ValueError("Invalid elements")
        self.element = element
        self.health = 100
        self.attack = 0
        self.armor = 0
        self.level = 1
        
    def __str__(self):
        return f"<{self.name} [{self.element}] ({self.health}, {self.attack}, {self.armor})>"
    
    def level_up(self):
        self.level += 1
        self.health = self.health * self.level
        
    def set_health(self, health=None):
        if health is None:
            self.health = 0
        elif not isinstance(health, int):
            raise ValueError("Health should be an integer")
        elif health <= 0:
            self.health = 0
        else:
            self.health = health

            
    def is_active(self):
        return self.health > 0
        
    def fight(self, pokemonB):
        while self.is_active() and pokemonB.is_active():
            # Print the health of each pokemon
            print(f"\n{self.name}{self.health}")
            print(f"{pokemonB.name}{pokemonB.health}\n")
            attack_A_to_B =  int(self.attack - pokemonB.armor)
            pokemonB.set_health = (pokemonB.health - attack_A_to_B)
            
            attack_B_to_A = int(pokemonB.attack - self.armor)
            self.set_health(self.health - attack_B_to_A)
            
    