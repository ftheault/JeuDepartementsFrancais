import random

from src.model.Department import generate_random_department
from src.model.EQuestionType import QuestionType


def generate_random_question_type():
    return QuestionType(random.randint(1, 3))


class Question:
    def __init__(self):
        self.random_department = generate_random_department()
        self.question_type = generate_random_question_type()
        self.text_edit_to_fill1 = ""
        self.text_edit_to_fill2 = ""
        self.text_edit_main_question = ""
        self.generate_random_question()

    def generate_random_question(self):
        if self.question_type == QuestionType.DEPARTMENT:
            self.text_edit_main_question = "Trouver le numéro de département et le chef-lieu associés au département suivant : " + self.random_department.name
            self.text_edit_to_fill1 = "Numéro de Département :"
            self.text_edit_to_fill2 = "Chef-lieu :"
        elif self.question_type == QuestionType.DEPARTMENT_NUMBER:
            self.text_edit_main_question = "Trouver le département et le chef-lieu associés au numéro de département suivant : " + str(
                self.random_department.number)
            self.text_edit_to_fill1 = "Département :"
            self.text_edit_to_fill2 = "Chef-lieu :"
        else:
            self.text_edit_main_question = "Trouver le département et le numéro de département associés au chef-lieu suivant : " + self.random_department.chief_town
            self.text_edit_to_fill1 = "Département :"
            self.text_edit_to_fill2 = "Numéro de département :"
