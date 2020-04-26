class Student:
    def __init__(self, name, score):
        if score < 0 or score > 100:
            raise Exception("Invalid Score")
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
        if self.score >= 55:
            return "D+"
        if self.score >= 50:
            return "D"
        if self.score >= 0:
            return "F"


assert str(Student("John", 80)) == "John"

assert Student("John", 80).get_grade() == "A"
assert Student("John", 79).get_grade() == "B+"
assert Student("John", 70).get_grade() == "B"
assert Student("John", 65).get_grade() == "C+"
assert Student("John", 60).get_grade() == "C"
assert Student("John", 55).get_grade() == "D+"
assert Student("John", 50).get_grade() == "D"

assert Student("John", 49).get_grade() == "F"
