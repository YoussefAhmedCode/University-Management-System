from models import student
from models.user import User
from storage.file_manager import load_data, save_data
import utils
from utils.id_generator import generate_teacher_id
from menus import teacher_edit_message
import json


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


    def view_assigned_courses(self, logged_in_teacher):
        teachers = load_data("data/teachers.json")
        for teacher in teachers:
            if teacher["teacher_id"] == logged_in_teacher["teacher_id"]:
                print("=" * 40)
                print("Assigned Courses")
                print("-" * 40)
                if len(teacher.get("courses", [])) == 0:
                    print("No Courses Assigned")
                else:
                    for course in teacher["courses"]:
                        print(course)
                return
        print("Teacher Not Found.")
    
    def view_enrolled_students(self, logged_in_teacher):
        courses = load_data("data/courses.json")
        students = load_data("data/students.json")
        course_id = input("Enter Course ID: ").strip()

        teacher_courses = logged_in_teacher.get("courses", [])
        is_assigned = False
        for course in teacher_courses:
            if course.lower() == course_id.lower():
                is_assigned = True
                break

        if not is_assigned:
            print("You are not assigned to teach this course.")
            return

        for course in courses:
            if course["course_id"].lower() == course_id.lower():
                enrolled_ids = course.get("enrolled_students", [])

                if not enrolled_ids:
                    print("No students are enrolled in this course.")
                    return

                print("=" * 40)
                print("Students Enrolled in", course["course_id"])
                print("=" * 40)

                for student_id in enrolled_ids:
                    found = False
                    for student in students:
                        if student["student_id"] == student_id:
                            print("ID:", student["student_id"], "| Name:", student["first_name"], student["last_name"])
                            found = True
                            break
                    if not found:
                        print("ID:", student_id, "| Name: Unknown")

                print("=" * 40)
                return

        print("Course Not Found.")

    def enter_grades(self, logged_in_teacher):
        courses = load_data("data/courses.json")
        students = load_data("data/students.json")
        course_id = input("Enter Course ID: ").strip()

        teacher_courses = logged_in_teacher.get("courses", [])
        is_assigned = False
        for course in teacher_courses:
            if course.lower() == course_id.lower():
                is_assigned = True
                break

        if not is_assigned:
            print("You are not assigned to teach this course.")
            return

        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid Student ID.")
            return

        enrolled = False
        for course in courses:
            if course["course_id"].lower() == course_id.lower():
                if student_id in course.get("enrolled_students", []):
                    enrolled = True
                break

        if not enrolled:
            print("Student is not registered in this course.")
            return

        try:
            grade_value = float(input("Enter Grade: "))
        except ValueError:
            print("Invalid Grade input.")
            return

        for student in students:
            if student["student_id"] == student_id:
                if "grades" not in student:
                    student["grades"] = {}
                student["grades"][course_id] = grade_value
                save_data("data/students.json", students)
                print("Grade Added Successfully")
                return

    def edit_grades(self, logged_in_teacher):
        courses = load_data("data/courses.json")
        students = load_data("data/students.json")
        course_id = input("Enter Course ID: ").strip()

        teacher_courses = logged_in_teacher.get("courses", [])
        is_assigned = False
        for course in teacher_courses:
            if course.lower() == course_id.lower():
                is_assigned = True
                break

        if not is_assigned:
            print("You are not assigned to teach this course.")
            return

        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid Student ID.")
            return

        for student in students:
            if student["student_id"] == student_id:
                if "grades" in student and course_id in student["grades"]:
                    try:
                        student["grades"][course_id] = float(input("Enter New Grade: "))
                    except ValueError:
                        print("Invalid Grade input.")
                        return

                    save_data("data/students.json", students)
                    print("Grade Updated Successfully")
                    return

        print("Record Not Found.")

   
