import random

from src.model.Department import Department, generate_random_department
from src.model.EQuestionType import QuestionType


def generate_random_question_type():
    return QuestionType(random.randint(1, 3))


class Question:
    def __init__(self):
        self.question_type = generate_random_question_type()
        self.main_question = self.generate_random_question()

    def generate_random_question(self):

        department = generate_random_department()

        if self.question_type == QuestionType.DEPARTMENT:
            return "Trouver le numéro de département et le chef-lieu associés au département suivant : " + department.name
        elif self.question_type == QuestionType.DEPARTMENT_NUMBER:
            return "Trouver le département et le chef-lieu associés au numéro de département suivant : " + department.number
        else:
            return "Trouver le département et le numéro de département associés au chef-lieu suivant : " + department.chief_town
