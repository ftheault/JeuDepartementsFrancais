import json
import random


def generate_random_department():
    return Department(random.randint(1, 101))


class Department:
    def __init__(self, number):
        self.number = number
        self.name = ""
        self.chief_town = ""
        self.retrieve_department_info_from_json_file()

    def retrieve_department_info_from_json_file(self):
        with open(
                'src/model/department.json') as department_file:  # Pour l'instant je lis à chaque fois le fichier .json mais il faudrait voir si c'est pas mieux de creer un disctionnaire juste une fois. Pour cela il faudrait peut-être crer une classe statique qui contient le dictionnaire python. Ou alors je le calcule une fois en local sous forme de string et je le stock dansn une classe
            departments = json.load(department_file)

        self.name = departments[self.number - 1]["nom"]
        self.chief_town = departments[self.number - 1]["codeRegion"]  # To modify
