import unittest
from src.student_management import StudentManagement

class TestStudentManagement(unittest.TestCase):
    def setUp(self):
        self.sm = StudentManagement()
        self.sample_student = ("S123", "Jan Kowalski", 21)
        self.valid_grades = [2.0, 3.0, 3.5, 4.0, 4.5, 5.0]

    # Testy dla add_student()
    def test_add_student_should_return_true_when_new_valid_student(self):
        # Act
        result = self.sm.add_student(*self.sample_student)
        # Assert
        self.assertTrue(result)

    def test_add_student_should_return_false_when_duplicate_id(self):
        # Arrange
        self.sm.add_student(*self.sample_student)
        # Act
        result = self.sm.add_student(self.sample_student[0], "Anna Nowak", 22)
        # Assert
        self.assertFalse(result)

    def test_add_student_should_return_false_when_invalid_age(self):
        # Act & Assert
        self.assertFalse(self.sm.add_student("S124", "Test", -5))
        self.assertFalse(self.sm.add_student("S125", "Test", 17.5))

    # Testy dla update_student()
    def test_update_student_should_return_true_when_existing_student(self):
        # Arrange
        self.sm.add_student(*self.sample_student)
        # Act
        result = self.sm.update_student(self.sample_student[0], "Jan Nowak", 22)
        # Assert
        self.assertTrue(result)

    def test_update_student_should_return_false_when_non_existing_id(self):
        # Act & Assert
        self.assertFalse(self.sm.update_student("NON_EXISTENT", "Test", 20))

    # Testy dla remove_student()
    def test_remove_student_should_return_true_when_existing_student(self):
        # Arrange
        self.sm.add_student(*self.sample_student)
        # Act
        result = self.sm.remove_student(self.sample_student[0])
        # Assert
        self.assertTrue(result)

    def test_remove_student_should_return_false_when_non_existing_id(self):
        # Act & Assert
        self.assertFalse(self.sm.remove_student("NON_EXISTENT"))

    # Testy dla add_grade()
    def test_add_grade_should_return_true_for_valid_grades(self):
        # Arrange
        self.sm.add_student(*self.sample_student)
        # Act & Assert
        for grade in self.valid_grades:
            self.assertTrue(self.sm.add_grade(self.sample_student[0], "Math", grade))

    def test_add_grade_should_return_false_for_invalid_grade(self):
        # Arrange
        self.sm.add_student(*self.sample_student)
        # Act & Assert
        self.assertFalse(self.sm.add_grade(self.sample_student[0], "Math", 1.5))
        self.assertFalse(self.sm.add_grade(self.sample_student[0], "Math", 6.0))

    # Testy dla avg_grades()
    def test_avg_grades_should_calculate_correct_average(self):
        # Arrange
        self.sm.add_student("S1", "A", 20)
        self.sm.add_student("S2", "B", 21)
        self.sm.add_grade("S1", "Math", 4.0)
        self.sm.add_grade("S1", "Math", 5.0)
        self.sm.add_grade("S2", "Math", 3.5)
        # Act
        avg = self.sm.avg_grades("Math")
        # Assert
        self.assertAlmostEqual(avg, (4.0 + 5.0 + 3.5) / 3, places=2)

    def test_avg_grades_should_return_zero_for_no_grades(self):
        # Act
        avg = self.sm.avg_grades("Physics")
        # Assert
        self.assertEqual(avg, 0.0)

if __name__ == "__main__":
    unittest.main()