from menus import student_edit_menu
from storage.file_manager import load_data, save_data
from utils.id_generator import generate_student_id
from models.student import Student
from models.user import User
from menus import student_edit_message


class StudentManager:

    def __init__(self):
        pass

    def add_student(self):

        first_name = input("Enter Student First Name: ").capitalize()
        last_name = input("Enter Student Last Name: ").capitalize()

        student_id = generate_student_id()

        email = str(student_id) + "@student.uni.edu"

        password = input("Enter Student Password: ")
        phone = input("Enter Student Phone: ")
        date_of_birth = input("Enter Student Date of Birth: ")

        departments = load_data("data/departments.json")

        while True:

            department_input = input("Enter Student Department: ").strip()

            found = False

            for department in departments:

                if department["name"].lower() == department_input.lower():

                    department_name = department["name"]
                    found = True
                    break

            if found:
                break

            print("Department does not exist.")

        gender = input("Enter Student Gender: ")
        academic_level = input("Enter Student Academic Level: ")

        student = Student(
            first_name,
            last_name,
            student_id,
            email,
            password,
            phone,
            date_of_birth,
            department_name,
            gender,
            academic_level,
        )

        user = User(email, password, "Student")

        students = load_data("data/students.json")
        students.append(student.to_dict())
        save_data("data/students.json", students)

        user.add_user()

        print("=" * 30)
        print("Student Added Successfully.")
        print("Student ID :", student.student_id)
        print("Email      :", student.email)
        print("=" * 30)

    def find_student_by_id(self):

        students = load_data("data/students.json")

        if not students:
            print("No Students Found.")
            return

        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid Input.")
            return

        for student in students:

            if student["student_id"] == student_id:

                print("=" * 30)

                for key, value in student.items():

                    if key == "password":
                        continue

                    print(key, ":", value)

                print("=" * 30)
                return

        print("Student Not Found.")

    def delete_student(self):

        students = load_data("data/students.json")
        users = load_data("data/users.json")
        courses = load_data("data/courses.json")

        try:
            student_id = int(input("Enter Student ID To Delete: "))
        except ValueError:
            print("Invalid Input.")
            return

        for student in students:

            if student["student_id"] == student_id:

                for user in users:

                    if user["email"] == student["email"]:
                        users.remove(user)
                        break

                course_list = student.get("courses", [])

                for course in courses:

                    if student_id in course.get("enrolled_students", []):
                        course["enrolled_students"].remove(student_id)

                students.remove(student)

                save_data("data/users.json", users)
                save_data("data/students.json", students)
                save_data("data/courses.json", courses)

                print("Student Deleted Successfully.")
                return

        print("Student Not Found.")

    def view_all_students(self):

        students = load_data("data/students.json")

        if not students:
            print("No Students Found.")
            return

        print("=" * 40)
        print("All Students")
        print("=" * 40)

        for student in students:

            for key, value in student.items():

                if key == "password":
                    continue

                print(key, ":", value)

            print("-" * 30)

    def edit_student_data(self):

        students = load_data("data/students.json")
        users = load_data("data/users.json")

        try:
            student_id = int(input("Enter Student ID To Update: "))
        except ValueError:
            print("Invalid Input.")
            return

        found = False

        for student in students:

            if student["student_id"] == student_id:

                found = True

                while True:

                    student_edit_menu()

                    choice = input("Enter Your Choice: ")

                    if choice == "1":

                        student["first_name"] = input(
                            "Enter New First Name: "
                        ).capitalize()

                        student_edit_message()

                    elif choice == "2":

                        student["last_name"] = input(
                            "Enter New Last Name: "
                        ).capitalize()

                        student_edit_message()

                    elif choice == "3":

                        student["password"] = input("Enter New Password: ")

                        for user in users:

                            if user["email"] == student["email"]:

                                user["password"] = student["password"]
                                break

                        save_data("data/users.json", users)

                        student_edit_message()

                    elif choice == "4":

                        student["phone"] = input("Enter New Phone: ")

                        student_edit_message()

                    elif choice == "5":

                        student["academic_level"] = input(
                            "Enter New Academic Level: "
                        )

                        student_edit_message()

                    elif choice == "0":
                        break

                    else:
                        print("Invalid Choice.")

                save_data("data/students.json", students)

                print("Student Updated Successfully.")
                return

        if not found:

            print("=" * 30)
            print("Student Not Found")
            print("=" * 30)

        def get_student_data(self, logged_in_user):

            students = load_data("data/students.json")

            for student in students:

                if student["email"] == logged_in_user["email"]:
                    return student

        return None

    def view_profile(self, logged_in_user):

        student = self.get_student_data(logged_in_user)

        if not student:
            print("Student Not Found.")
            return

        print("=" * 30)
        print("Student Profile")
        print("=" * 30)

        for key, value in student.items():

            if key == "password":
                continue

            print(key.replace("_", " ").title(), ":", value)

    def view_courses(self, logged_in_user):

        student = self.get_student_data(logged_in_user)

        if not student:
            print("Student Not Found.")
            return

        enrolled_courses = student.get("courses", [])

        if not enrolled_courses:
            print("You are not registered in any courses.")
            return

        courses = load_data("data/courses.json")

        print("=" * 40)
        print("Registered Courses")
        print("=" * 40)

        for course in courses:

            if course["course_id"] in enrolled_courses:

                print("Course ID   :", course["course_id"])
                print("Course Name :", course["course_name"])
                print("Department  :", course["department"])
                print("Credit Hours:", course["credit_hours"])
                print("-" * 30)

    def view_grades(self, logged_in_user):

        student = self.get_student_data(logged_in_user)

        if not student:
            print("Student Not Found.")
            return

        grades = student.get("grades", {})

        if not grades:
            print("No Grades Available.")
            return

        courses = load_data("data/courses.json")

        print("=" * 40)
        print("Grades")
        print("=" * 40)

        for course_id in grades:

            course_name = course_id

            for course in courses:

                if course["course_id"] == course_id:
                    course_name = course["course_name"]
                    break

            print(course_name, ":", grades[course_id])

    def view_attendance(self, logged_in_user):

        student = self.get_student_data(logged_in_user)

        if not student:
            print("Student Not Found.")
            return

        attendance = load_data("data/attendance.json")

        found = False

        courses = load_data("data/courses.json")

        print("=" * 40)
        print("Attendance")
        print("=" * 40)

        for record in attendance:

            if record["student_id"] == student["student_id"]:

                found = True

                course_name = record["course_id"]

                for course in courses:

                    if course["course_id"] == record["course_id"]:
                        course_name = course["course_name"]
                        break

                print("Course :", course_name)
                print("Status :", record["status"])
                print("-" * 30)

        if not found:
            print("No Attendance Records Found.")