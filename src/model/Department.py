import json
import random


def generate_random_department():
    random_department = Department(number=random.randint(1, 101))
    random_department.retrieve_department_info_from_json_file()
    return random_department


class Department:
    def __init__(self, name="", number=None, chief_town=""):
        self.name = name
        self.number = number
        self.chief_town = chief_town

    def retrieve_department_info_from_json_file(self):
        with open(
                'src/model/department.json') as department_file:  # Pour l'instant je lis à chaque fois le fichier .json mais il faudrait voir si c'est pas mieux de creer un disctionnaire juste une fois. Pour cela il faudrait peut-être crer une classe statique qui contient le dictionnaire python. Ou alors je le calcule une fois en local sous forme de string et je le stock dansn une classe
            departments = json.load(department_file)
        for d in departments:
            if d["code"] == "2A" or d["code"] == "2B":
                continue
            elif int(d["code"]) == self.number:
                self.name = d["nom"]
                self.chief_town = d["chef-lieu"]  # To modify
                return

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name and int(self.number) == int(
                other.number) and self.chief_town == other.chief_town

    def __ne__(self, other):
        return not self.__eq__(other)
