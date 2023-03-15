# import csv

# # class Quiz:
# #     def __init__(self, file="quiz1.txt"):
# #         self.file = file
# #         with open("quiz1.txt", "r") as f:
# #             reader = csv.reader(f)
# #             data = list(reader)
# #             self.data = data
            
    
#     # def get_question(self, number):
#     #     if not isinstance(number, int):
#     #         return None
#     #     if number < 1 or number > len(self.questions):
#     #         return None
    
#     def get_question(self, number):
#         if not isinstance(number, int):
#             return None
#         if number < 1 or number > len(self.questions):
#             return None
#         return self.questions[number - 1]
    
#     def get_full_question(self):
#         for key, index in enumerate(self.question):
#             print(question)
#             for 

# questions = []
# answers = []
# correct_answers = []
# with open("quiz1.txt", 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         questions.append(row[0])
#         answers.append(row[1:4])
#         correct_answers.append(row[5])

# print(questions)
# print(answers)
# print(correct_answers)

#     def fight(self, pokemonB):
#         while self.is_active() and pokemonB.is_active():
#             print(f"\n{self.name}({self.health})")
#             print(f"{pokemonB.name}({pokemonB.health})\n")

#             attack_A_to_B = self.attack - pokemonB.armor
#             if self.element == "fire" and pokemonB.element == "grass":
#                 attack_A_to_B *= 2
#             elif self.element == "water" and pokemonB.element == "fire":
#                 attack_A_to_B *= 2
#             elif self.element == "grass" and pokemonB.element == "water":
#                 attack_A_to_B *= 2
#             elif self.element == "electric" and pokemonB.element == "water":
#                 attack_A_to_B *= 2
#             elif self.element == "water" and pokemonB.element == "electric":
#                 attack_A_to_B *= 2
#             elif self.element == "electric" and pokemonB.element == "grass":
#                 attack_A_to_B *= 2
#             pokemonB.set_health(pokemonB.health - attack_A_to_B)

#             attack_B_to_A = pokemonB.attack - self.armor
#             if pokemonB.element == "fire" and self.element == "grass":
#                 attack_B_to_A *= 2
#             elif pokemonB.element == "water" and self.element == "fire":
#                 attack_B_to_A *= 2
#             elif pokemonB.element == "grass" and self.element == "water":
#                 attack_B_to_A *= 2
#             elif pokemonB.element == "electric" and self.element == "water":
#                 attack_B_to_A *= 2
#             elif pokemonB.element == "water" and self.element == "electric":
#                 attack_B_to_A *= 2
#             elif pokemonB.element == "electric" and self.element == "grass":
#                 attack_B_to_A *= 2
#             self.set_health(self.health - attack_B_to_A)