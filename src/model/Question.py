import random

from src.model.QuestionType import QuestionType


def generate_random_question_type():
    return QuestionType(random.randint(1, 3))


class Question:
    def __init__(self):
        self.question_type = generate_random_question_type()
        self.main_question = ""

    def generate_random_question(self,):
        if self.question_type == QuestionType.DEPARTMENT:
            return ""
        elif self.question_type == QuestionType.DEPARTMENT_NUMBER:
            return ""
        else:
            return ""
