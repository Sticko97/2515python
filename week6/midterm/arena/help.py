import csv

with open('pokemons.txt') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['name']
        health = int(row['health'])
        level = int(row['level'])
        
print(row)

"""
I READ TESTS AND INSTRUCTIONS
consider pokemon type advantage into the pokemon class.
in the fight method, pokemon may deal super effective damage and vice versa


"""