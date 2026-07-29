from storage.file_manager import load_data, save_data


class Course:

    def __init__(
        self,
        course_id,
        course_name,
        department,
        credit_hours,
        teacher_ids=None,
        enrolled_students=None,
    ):

        self.course_id = course_id
        self.course_name = course_name
        self.department = department
        self.credit_hours = credit_hours

        if teacher_ids is None:
            self.teacher_ids = []
        else:
            self.teacher_ids = teacher_ids

        if enrolled_students is None:
            self.enrolled_students = []
        else:
            self.enrolled_students = enrolled_students

    def to_dict(self):

        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "department": self.department,
            "credit_hours": self.credit_hours,
            "teacher_ids": self.teacher_ids,
            "enrolled_students": self.enrolled_students,
        }

    def display(self):
        print("=" * 30)
        print("Course ID:", self.course_id)
        print("Course Name:", self.course_name)
        print("Department:", self.department)
        print("Credit Hours:", self.credit_hours)

        if self.teacher_ids:
            print("Teachers:", ", ".join(map(str, self.teacher_ids)))
        else:
            print("Teachers: None")

        print("No. Enrolled Students:", len(self.enrolled_students))

    def display_students(self):
        print("=" * 30)
        print("Enrolled Students")
        print("=" * 30)

        if not self.enrolled_students:
            print("No students enrolled.")
            return

        for student in self.enrolled_students:
            print(student)

    def display_teachers(self):
        print("=" * 30)
        print("Assigned Teachers")
        print("=" * 30)

        if not self.teacher_ids:
            print("No teachers assigned.")
            return

        for teacher in self.teacher_ids:
            print(teacher)
    
    


