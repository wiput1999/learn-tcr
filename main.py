class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return self.name

    def get_grade(self):
        if self.score >= 80:
            return "A"
        return "F"


assert str(Student("John", 80)) == "John"
