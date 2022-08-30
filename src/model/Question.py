import random

from src.model.QuestionType import QuestionType


class Question:
    def __init__(self):
        self.question_type = ""
        self.main_question = ""

    def generate_random_question_type(self):
         return QuestionType(random.randint(1, 3))

    def generate_random_question(self, question_type):
        if question_type == QuestionType.DEPARTMENT:
            return ""
        elif question_type == QuestionType.DEPARTMENT_NUMBER:
            return ""
        else:
            return ""