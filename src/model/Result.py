class Answer:
    def __init__(self, question_department, user_response_department):
        self.user_response_department = user_response_department
        self.question_department = question_department

    def checking(self):
        if self.user_response_department == self.question_department:
            return True
        else:
            return False