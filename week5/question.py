import random

class Question:
    """Question class represents a multiple choice question with
    a question prompt, a correct answer, and a list of incorrect answers.
    """
    def __init__(self, question, correct_answer, incorrect_answers, category, difficulty):
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers
        self.category = category
        self.difficulty = difficulty
        if self.difficulty not in ["easy", "medium", "hard"]:
            raise AttributeError("Difficulties are easy, medium, or hard")
        self.answers = incorrect_answers + [correct_answer]
        random.shuffle(self.answers)
        self.answer_id = self.answers.index(correct_answer)

    def __str__(self):
        """
        method displays the question in Dunder method __init__,
        is able to display the index of correct answers, starting index is set to 1 instead of 0
        print formatted by new line '\n'
        """
        answer_string = ""
        for i, answer in enumerate(self.answers, start=1):
            answer_string += f"{i}. {answer}\n"
        return f"{self.question}\n{answer_string}"
        

