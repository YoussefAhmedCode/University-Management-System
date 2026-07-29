from models.user import User


class Student(User):
    def __init__(
        self,
        first_name,
        last_name,
        student_id,
        email,
        password,
        phone,
        date_of_birth,
        department,
        gender,
        academic_level,
        courses=None,
        role="Student",
    ):
        super().__init__(email, password, role)

        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.department = department
        self.gender = gender
        self.academic_level = academic_level

        if courses is None:
            self.courses = []
        else:
            self.courses = courses

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
            "role": self.role,
            "phone": self.phone,
            "date_of_birth": self.date_of_birth,
            "department": self.department,
            "gender": self.gender,
            "academic_level": self.academic_level,
            "courses": self.courses,
        }

    def display(self):
        print("=" * 30)
        print("Student ID:", self.student_id)
        print("Name:", self.first_name, self.last_name)
        print("Email:", self.email)
        print("Phone:", self.phone)
        print("Date of Birth:", self.date_of_birth)
        print("Department:", self.department)
        print("Gender:", self.gender)
        print("Academic Level:", self.academic_level)
        
    def display_courses(self, logged_in_student):
        print("Registered Courses:", logged_in_student["courses"])
