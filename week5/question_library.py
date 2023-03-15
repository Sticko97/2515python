import json
import random
from question import Question
from unittest.mock import patch, mock_open


class QuestionLibrary:
    """
    This class loads a JSON file, and holds all available questions. 
    Stores JSON file into lists with two methods that retrieve questions and categories
    """
    def __init__(self, filename="trivia.json"):
        self.questions = []
        self.categories = []
        with open(filename, "r") as f:
            self.questions_data = json.load(f)
        for parameter in self.questions_data:
            question = Question(
                parameter["question"],
                parameter["correct_answer"],
                parameter["incorrect_answers"],
                parameter["category"],
                parameter["difficulty"],
            )
            self.questions.append(question)

    def __len__(self):
        """Dunder method len, allows len() call to work on class QuestionLibrary
        """
        return len(self.questions)
    
    def get_categories(self):
        """
        Sets category variable to equal category key in json string
        """
        for parameter in self.questions_data:
            category = parameter["category"]
            if category not in self.categories:
                self.categories.append(category)
        return self.categories
    
    def get_questions(self, category=None, difficulty=None, number=None): #time taken to complete ~5+ days 
        """
        a category (str): the name of the category to filter questions (ex: "Geography")
        a difficulty (str): the difficulty level to filter questions. Can be "easy", "medium", or "hard". If it is something
        else, ignore the argument
        Returns:
            int: the number of filtered questions to return. If not provided, return all questions available
        """
        questions = []
        challenge = ["easy","medium", "hard"]
        if difficulty not in challenge:
            difficulty = None #sets difficulty to none in order to ignore the argument
        for question in self.questions:
            if (question.category == category or category is None) and (question.difficulty.lower() == difficulty or difficulty is None):
                questions.append(question)
        random.shuffle(questions)
        return questions[:number]
    