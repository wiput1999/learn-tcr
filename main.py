import unittest


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


class StudentCollection:
    pass


class StudentTest(unittest.TestCase):
    def test_grade_a(self):
        self.assertEqual(Student("John", 80).get_grade(), "A")

    def test_grade_b_plus(self):
        self.assertEqual(Student("John", 75).get_grade(), "B+")

    def test_grade_b(self):
        self.assertEqual(Student("John", 70).get_grade(), "B")

    def test_grade_c_plus(self):
        self.assertEqual(Student("John", 65).get_grade(), "C+")

    def test_grade_c(self):
        self.assertEqual(Student("John", 60).get_grade(), "C")

    def test_grade_d_plus(self):
        self.assertEqual(Student("John", 55).get_grade(), "D+")

    def test_score_error_high(self):
        with self.assertRaises(Exception) as context:
            Student("John", 101)
        self.assertTrue(context.exception)

    def test_score_error_low(self):
        with self.assertRaises(Exception) as context:
            Student("John", -1)
        self.assertTrue(context.exception)


unittest.main()
