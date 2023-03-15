import json
import random
from question import Question
from question_library import QuestionLibrary

# empty = []
# with open("trivia.json", "r") as f:
#     file = json.load(f)
#     for item in file:
#         for i, element in enumerate(item["category"]):
#             empty.append(element)
#     # print(empty)
#     en = empty
#     print(set(file[0])) #"""prints keys"""
#     # print(en)
    
    # for question in file:
    #     category = question["category"]
    # if category not in empty:
    #     empty.append(category)
    
    # print(len(empty))
    
    # def get_categories(self):
    #     """
    #     Sets category variable to equal category key in json string
    #     """
    #     for parameter in self.questions_data:
    #         category = parameter["category"]
    #         if category not in self.categories:
    #             self.categories.append(category)
    #     return self.categories
    
    # def get_questions(self, category=None, difficulty=None, number=None):
    #     """consider possibilities, category provided, difficulty, neither or both"""
    #     questions = []
    #     for parameter in self.questions:
    #         if not category and not difficulty:
    #             questions.append(parameter)
    #         elif not category:
    #             if parameter["difficulty"] == difficulty:
    #                 questions.append(parameter)
    #         elif not difficulty:
    #             if parameter["category"] == category:
    #                 questions.append(parameter)
    #         elif parameter["category"] == category or parameter["difficulty"] == difficulty:
    #             questions.append(parameter)
    #     return questions[:number] if number is not None else questions
    
    # def get_questions(self, category=None, difficulty=None, number=None):
    #     questions = []
    #     for question in self.questions: # q = index of Question class list containing json.file
    #         if difficulty not in ["easy","medium", "hard"] and difficulty is not None:
    #             continue
    #     for question in self.questions_data: # q = index of self.questions_data/json.file
    #         question = q["question"] # set question variable to index:key matching "question" item
    #         if question not in category and not difficulty: # if key not in category or difficulty, append it to new list
    #             questions.append(q)
    #         elif question not in category:# if not in category, set key of difficulty to difficulty
    #             if q["difficulty"] == difficulty:
    #                 questions.append(q)
    #         elif question not in difficulty:#if not in difficulty
    #             if q["category"] == category:# if key of category matches category, append key to list
    #                 questions.append(q)
    #         elif question.category == category and question.difficulty == difficulty:
    #             questions.append(question)
    #         elif question.category == category or question.difficulty == difficulty:#check to see if it meets the requirements, easy,medium,hard orelse it wont work
    #             questions.append(question)
    #     random.shuffle(questions) 
    #     return questions[:number] if number is not None else questions
        
    # def get_questions(self, category=None, difficulty=None, number=None):
    #     questions = []
    #     challenge = ["easy","medium", "hard"]
    #     if difficulty not in challenge and difficulty is not None:
    #         difficulty = [challenge in questions] #"""difficulty = [q.difficulty for q in lib.questions]"""
    #     for question in self.questions:
    #         # if question not in challenge and difficulty is not None:
    #             # return len(self.questions)
    #         if question.category == category and question.difficulty == difficulty:
    #             questions.append(question)
    #         elif question.category == category or question.difficulty == difficulty:#check to see if it meets the requirements, easy,medium,hard orelse it wont work
    #             questions.append(question)
    #     random.shuffle(questions) 
    #     return questions[:number] if number is not None else questions
    
    def play(self):
        """Play method, checks to see if player input is correct and increases score instance based on difficulty of question
        player input is an integer from 1 to 4
        if player input is not an integer from 1 to 4, player is raised a ValueError and is prompted to try again.
        """
        choice = [1, 2, 3, 4]
        for question in self.questions:
            print(question)
            # print(f'{question.question} \nAnswer Options:')
            # for i, item in enumerate(question.answers):
            #     print(f"{i + 1}: {item}")
            # # player_input = int(input(f"input from {choice}: "))
            player_input = input('Enter an answer from 1-4')
            while player_input not in ['1','2','3','4']:
                player_input = input(f"Select answer {choice}: ")
            if int(player_input) == question.answer_id:
                print(f"Correct!")
                print(f"{question.difficulty}")
                if question.difficulty == "easy":
                    self.score += 1
                elif question.difficulty == "medium":
                    self.score += 2
                elif question.difficulty == "hard":
                    self.score += 3
            else:
                print(f"Incorrect!")
                print(f"{question.difficulty}")
                # except ValueError:
                    # print(f"Invalid Answer. Please choose from {choice}")
                    # player_input = None
        print(f"Final score:{self.score}")
        
            def play(self):
        """Play method, checks to see if player input is correct and increases score instance based on difficulty of question
        player input is an integer from 1 to 4
        if player input is not an integer from 1 to 4, player is raised a ValueError and is prompted to try again.
        """
        choice = [1, 2, 3, 4]
        for question in self.questions:
            print(question)
            # print(f'{question.question} \nAnswer Options:')
            # for i, item in enumerate(question.answers):
            #     print(f"{i + 1}: {item}")
            # # player_input = int(input(f"input from {choice}: "))
            player_input = input('Enter an answer from 1-4')
            while player_input not in ['1', '2','3','4']:
                player_input = input(f"Select answer {choice}: ")
            if int(player_input) == question.answer_id:
                print(f"Correct!")
                print(f"{question.difficulty}")
                if question.difficulty == "easy":
                    self.score += 1
                elif question.difficulty == "medium":
                    self.score += 2
                elif question.difficulty == "hard":
                    self.score += 3
            else:
                print(f"Incorrect!")
                print(f"{question.difficulty}")
                # except ValueError:
                    # print(f"Invalid Answer. Please choose from {choice}")
                    # player_input = None
        print(f"Final score:{self.score}")