from models.user import User



class Teacher(User):
    def __init__(
        self,
        first_name,
        last_name,
        teacher_id,
        email,
        password,
        phone,
        department,
        office,
        role="Teacher",
        courses=None,
    ):
        super().__init__(email, password, role)
        self.first_name = first_name
        self.last_name = last_name
        self.teacher_id = teacher_id
        self.phone = phone
        self.department = department
        self.office = office
        if courses is None:
            self.courses = []
        else:
            self.courses = courses

    def to_dict(self):
        teacher = {
            "teacher_id": self.teacher_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
            "phone": self.phone,
            "department": self.department,
            "office": self.office,
            "courses": self.courses,
        }
        return teacher

    def display(self):
        print("=" * 30)
        print("Teacher ID:", self.teacher_id)
        print("Name:", self.first_name, self.last_name)
        print("Email:", self.email)
        print("Phone:", self.phone)
        print("Department:", self.department)
        print("Office:", self.office)