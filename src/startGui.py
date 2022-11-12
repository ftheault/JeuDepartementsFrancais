from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

import src.view.startGUI
from src.model.Department import Department
from src.model.EQuestionType import QuestionType
from src.model.Question import Question
from src.model.Result import Answer


class LaunchGame(QtWidgets.QMainWindow, src.view.startGUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(LaunchGame, self).__init__(parent)
        self.setupUi(self)
        # self.show()
        self.showMaximized()
        self.question = None
        self.display_random_question()
        self.pushButtonToValidate.clicked.connect(self.check_response)
        # self.labelImageFranceMap.setPixmap(QPixmap("french-map.png"))

    def display_random_question(self):
        self.question = Question()
        self.textEditQuestion.setText(self.question.text_edit_main_question)
        self.textEditInformation1.setText(self.question.text_edit_to_fill1)
        self.textEditInformation2.setText(self.question.text_edit_to_fill2)

    def get_answer(self):
        if self.question.question_type == QuestionType.DEPARTMENT:
            department_number_response = self.textEditFieldToComplete1.toPlainText()
            department_chief_town_response = self.textEditFieldToComplete2.toPlainText()
            department_response = Department(self.question.random_department.name, int(department_number_response),
                                             department_chief_town_response)
        elif self.question.question_type == QuestionType.DEPARTMENT_NUMBER:
            department_name_response = self.textEditFieldToComplete1.toPlainText()
            department_chief_town_response = self.textEditFieldToComplete2.toPlainText()
            department_response = Department(department_name_response, self.question.random_department.number,
                                             department_chief_town_response)
        else:
            department_name_response = self.textEditFieldToComplete1.toPlainText()
            department_number_response = self.textEditFieldToComplete2.toPlainText()
            department_response = Department(department_name_response, int(department_number_response),
                                             self.question.random_department.chief_town)
        return department_response

    def check_response(self):
        if self.textEditFieldToComplete1.toPlainText() == "" or self.textEditFieldToComplete2.toPlainText() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please fill all the fields")
            msg.setWindowTitle("Missing information")
            msg.show()
            msg.exec()
        else:
            result = Answer(self.question.random_department, self.get_answer())

            if result.checking():
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Bien joué !!!!!!")
                msg.setWindowTitle("Result")
                msg.show()
                msg.exec()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("T'es nul en fait !!!!!!")
                msg.setWindowTitle("Result")
                msg.show()
                msg.exec()

            self.display_random_question()
