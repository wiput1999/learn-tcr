class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return self.name


assert str(Student("John", 80)) == "John"
