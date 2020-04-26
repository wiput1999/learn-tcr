class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return self.name

    def get_grade(self):
        if self.score >= 80:
            return "A"
        if self.score >= 75:
            return "B+"
        if self.score >= 70:
            return "B"
        if self.score >= 65:
            return "C+"
        if self.score >= 60:
            return "C"
        return "F"


assert str(Student("John", 80)) == "John"

assert Student("John", 80).get_grade() == "A"
assert Student("John", 79).get_grade() == "B+"
assert Student("John", 70).get_grade() == "B"
assert Student("John", 65).get_grade() == "C+"
assert Student("John", 60).get_grade() == "C"

assert Student("John", 49).get_grade() == "F"
