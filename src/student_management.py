class StudentManagement:
    def __init__(self):
        self.students = {}  # {id: {"name": str, "age": int}}
        self.grades = {}  # {subject: {student_id: [grades]}}

    def add_student(self, id: str, name: str, age: int) -> bool:
        if id in self.students or not isinstance(age, int) or age <= 0:
            return False

        self.students[id] = {"name": name, "age": age}
        return True

    def update_student(self, id: str, name: str, age: int) -> bool:
        if id not in self.students or not isinstance(age, int) or age <= 0:
            return False

        self.students[id] = {"name": name, "age": age}
        return True

    def remove_student(self, id: str) -> bool:
        if id not in self.students:
            return False

        del self.students[id]
        # Usuń wszystkie oceny studenta
        for subject in self.grades.values():
            if id in subject:
                del subject[id]
        return True

    def add_grade(self, student_id: str, subject: str, grade: float) -> bool:
        if student_id not in self.students:
            return False

        valid_grades = {2.0, 3.0, 3.5, 4.0, 4.5, 5.0}
        if grade not in valid_grades:
            return False

        if subject not in self.grades:
            self.grades[subject] = {}

        if student_id not in self.grades[subject]:
            self.grades[subject][student_id] = []

        self.grades[subject][student_id].append(grade)
        return True

    def avg_grades(self, subject: str) -> float:
        if subject not in self.grades:
            return 0.0

        total = 0
        count = 0
        for student_grades in self.grades[subject].values():
            total += sum(student_grades)
            count += len(student_grades)

        return round(total / count, 2) if count > 0 else 0.0