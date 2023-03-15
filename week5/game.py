import json
import random
from question import Question
from question_library import QuestionLibrary
from unittest.mock import patch

class Game:
    def __init__(self, filename="trivia.json", category=None, difficulty=None, number=None):
        """QuestionLibrary is imported as well as get_questions()
        instance of question_library.get_questions() to get questions with category, difficulty and number
        implements an instance where score is set to 0
        
        Args:
            filename (str, optional): Defaults to "trivia.json".
            category (_type_, optional): Defaults to None.
            difficulty (_type_, optional): Defaults to None.
            number (_type_, optional): Defaults to None.
        """
        question_library = QuestionLibrary(filename)
        self.questions = question_library.get_questions(category, difficulty, number)
        self.score = 0
        
        
    def play(self):
        """Play method, checks to see if player input is correct and increases score instance based on difficulty of question
        player input is an integer from 1 to 4
        if player input is not an integer from 1 to 4, player is raised a ValueError and is prompted to try again.
        """
        choice = [1, 2, 3, 4]
        choice_string = ["1","2","3","4"]
        for question in self.questions:
            print(f'{question.question} \nAnswer Options:')
            for i, item in enumerate(question.answers):
                print(f"{i + 1}: {item}")
            player_input = input(f"Input from {choice}: ")
            while player_input not in choice_string:
                    player_input = input(f"Select answer {choice}: ")
                    print(f"Invalid Answer. Please choose from {choice}")
            if int(player_input) == question.answer_id:
                print(f"Correct!")
                if question.difficulty == "easy":
                    self.score += 1
                    print(f"{self.score}")
                elif question.difficulty == "medium":
                    self.score += 2
                    print(f"{self.score}")
                elif question.difficulty == "hard":
                    self.score += 3
                    print(f"{self.score}")
            else:
                print(f"Incorrect!, your score is {self.score}")
        print(f"Final score: {self.score}")
        
        
                    
                
        


            

        
    
    
        