class Student:
    def __init__(self):
        self.name = "Hello"

    def __str__(self):
        return self.name


assert str(Student()) == "Hello"
