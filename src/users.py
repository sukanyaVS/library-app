class User:
    def __init__(self):
        pass

    def can_issue(self):
        return False

class Student(User):
    def can_issue(self):
        return True

class Admin(User):
    def can_issue(self):
        return False
