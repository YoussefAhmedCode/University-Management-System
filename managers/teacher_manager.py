from models.user import User
from storage.file_manager import load_data, save_data
from models.teacher import Teacher
from menus import teacher_edit_menu, teacher_edit_message
from utils.id_generator import generate_teacher_id
from models.attendance import attendance


class TeacherManager:

    def __init__(self):
        pass

    def add_teacher(self):

        first_name = input("Enter Teacher First Name: ").capitalize()
        last_name = input("Enter Teacher Last Name: ").capitalize()
        password = input("Enter Teacher Password: ")
        phone = input("Enter Teacher Phone: ")

        departments_data = load_data("data/departments.json")

        while True:

            department_input = input("Enter Teacher Department: ").strip()
            found_dept = False

            for dept in departments_data:

                if dept["name"].lower() == department_input.lower():
                    found_dept = True
                    department = dept["name"]
                    break

            if found_dept:
                break

            print(
                "Error: Department",
                department_input,
                "doesn't exist. Please enter a valid department.",
            )

        office = input("Enter Teacher Office: ")

        teacher_id = generate_teacher_id()

        email = str(teacher_id) + "@teacher.uni.edu"

        teacher = Teacher(
            first_name,
            last_name,
            teacher_id,
            email,
            password,
            phone,
            department,
            office,
        )

        user = User(email, password, role="Teacher")
        user.add_user()

        teachers = load_data("data/teachers.json")

        teachers.append(teacher.to_dict())

        save_data("data/teachers.json", teachers)

        print("=" * 30)
        print("Dr/",teacher.first_name, teacher.last_name, "has been added successfully.")
        print("Teacher ID:", teacher.teacher_id)
        print("Email:", teacher.email)
        print("=" * 30)

        return teacher
    
    def view_all_teachers(self):

        teachers = load_data("data/teachers.json")

        if len(teachers) == 0:
            print("No teachers found.")
            return

        print("All Teachers:")

        for teacher in teachers:

            print("-" * 20)

            for key, value in teacher.items():

                if key == "password":
                    continue

                print(key, ":", value)

            print("-" * 20)

    def search_teacher(self):

        teachers = load_data("data/teachers.json")

        try:

            teacher_id = int(input("Enter Teacher ID to search: "))

        except ValueError:
            print("Invalid input.")
            return

        found = False

        for teacher in teachers:

            if teacher["teacher_id"] == teacher_id:

                found = True

                print("=" * 30)
                print("Found Teacher:")
                print("=" * 30)

                for key, value in teacher.items():

                    if key == "password" or key == "role":
                        continue

                    print(key, ":", value)

                return

        if not found:
            print("There is no teacher with this ID!")
            
            
    def edit_teacher(self):
            teachers = load_data("data/teachers.json")
            users = load_data("data/users.json")
    
            try:
    
                teacher_id = int(input("Enter Teacher ID: "))
                found = False
    
                for teacher in teachers:
                    if teacher["teacher_id"] == teacher_id:
                        found = True
                        while True:
                            teacher_edit_menu()
                            choice = input("Enter Your choice: ")
    
                            if choice == "1":
                                teacher["first_name"] = input("Enter New First Name: ")
                                teacher_edit_message()
    
                            elif choice == "2":
                                teacher["last_name"] = input("Enter New Last Name: ")
                                teacher_edit_message()
    
                            elif choice == "3":
                                for user in users:
                                    if user["email"] == teacher["email"]:
                                        teacher["password"] = input("Enter New password: ")
                                        user["password"] = teacher["password"]
                                        teacher_edit_message()
                                        save_data("data/users.json", users)
                                        break
    
                            elif choice == "4":
                                teacher["office"] = input("Enter New office: ")
                                teacher_edit_message()
    
                            elif choice == "5":
                                teacher["phone"] = input("Enter New Phone: ")
                                teacher_edit_message()
    
                            elif choice == "0":
                                break
    
                            else:
                                print("Invalid choice.")
                                continue
    
                        save_data("data/teachers.json", teachers)
                        return
    
                if found == False:
                    print("=" * 30)
                    print("Teacher Not Found")
                    print("=" * 30)
            except ValueError:
                print("Invaild input.")

    def delete_teacher(self):

        teachers = load_data("data/teachers.json")
        users = load_data("data/users.json")
        courses = load_data("data/courses.json")

        try:

            teacher_id = int(input("Enter Teacher ID to Delete: "))

        except ValueError:
            print("Invalid input.")
            return

        for teacher in teachers:

            if teacher["teacher_id"] == teacher_id:

                for course in courses:

                    if teacher_id in course.get("teacher_ids", []):

                        course["teacher_ids"].remove(teacher_id)

                save_data("data/courses.json", courses)

                for user in users:

                    if user["email"] == teacher["email"]:

                        users.remove(user)
                        save_data("data/users.json", users)
                        break

                teachers.remove(teacher)

                save_data("data/teachers.json", teachers)

                print("Teacher deleted successfully.")

                return

        print("Teacher not found.")



    def assign_course(self):

        teachers = load_data("data/teachers.json")
        courses = load_data("data/courses.json")

        try:
            teacher_id = int(input("Enter Teacher ID: "))
        except ValueError:
            print("Invalid Teacher ID.")
            return

        course_id = input("Enter Course ID: ").strip().upper()

        found_teacher = False
        found_course = False

        for teacher in teachers:

            if teacher["teacher_id"] == teacher_id:

                found_teacher = True

                for course in courses:

                    if course["course_id"].upper() == course_id.upper():

                        found_course = True


                        if teacher["department"].title() != course["department"].title():
                            print("Teacher and Course Departments Do Not Match.")
                            return

                        if course_id in teacher["courses"]:
                            print("Course Already Assigned.")
                            return

                        if teacher_id in course["teacher_ids"]:
                            print("Teacher Already Assigned To This Course.")
                            return

                        teacher["courses"].append(course_id)
                        course["teacher_ids"].append(teacher_id)

                        save_data("data/teachers.json", teachers)
                        save_data("data/courses.json", courses)

                        print("Course Assigned Successfully.")
                        return

                break

        if not found_teacher:
            print("Teacher Not Found.")
        elif not found_course:
            print("Course Not Found.")
            
    def get_teacher_data(self, logged_in_user):
        teachers = load_data("data/teachers.json")
        for teacher in teachers:
            if teacher["email"] == logged_in_user["email"]:
                return teacher
        return None

    def view_assigned_courses(self, logged_in_user):
        
        teacher = self.get_teacher_data(logged_in_user)
        
        if not teacher:
            print("Teacher not found.")
            return
        
        print("=" * 40)
        print("Assigned Courses")
        print("-" * 40)
        
        if not teacher.get("courses", []):
            print("No Courses Assigned")
        else:
            for course in teacher["courses"]:
                print(course)

    def view_enrolled_students(self, logged_in_user):

        teacher = self.get_teacher_data(logged_in_user)
        courses = load_data("data/courses.json")
        students = load_data("data/students.json")

        if not teacher:
            print("Teacher Not Found.")
            return

        course_id = input("Enter Course ID: ").strip().upper()

        found_course = False
        assigned = False

        for teacher_course in teacher["courses"]:

            if teacher_course.upper() == course_id.upper():
                assigned = True
                break

        if not assigned:
            print("You are not assigned to teach this course.")
            return

        for course in courses:

            if course["course_id"].upper() == course_id.upper():

                found_course = True

                if not course["enrolled_students"]:
                    print("No Students Are Enrolled In This Course.")
                    return

                print("=" * 40)
                print("Students Enrolled In", course["course_id"])
                print("=" * 40)
                
                for student_id in course["enrolled_students"]:
                
                    for student in students:
                
                        if student["student_id"] == student_id:
                
                            print(
                                "ID:",
                                student["student_id"],
                                "| Name:",
                                student["first_name"],
                                student["last_name"],
                            )
                            
                            print("=" * 40)
                            break
                
        if not found_course:
            print("Course Not Found.")
            return


    def enter_grades(self, logged_in_user):
        teacher = self.get_teacher_data(logged_in_user)
        
        assigned=False
        
        if not teacher:
            print("Teacher not found.")
            return
        
        courses = load_data("data/courses.json")
        students = load_data("data/students.json")
        
        course_id = input("Enter Course ID: ").strip().upper()
        
        for teacher_course in teacher["courses"]:

            if teacher_course.upper() == course_id.upper():
                assigned = True
                break

        if not assigned:
            print("You are not assigned to teach this course.")
            return
        
        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid Student ID.")
            return
        
        enrolled = False
        
        for course in courses:
            if course["course_id"].upper() == course_id.upper():
                if student_id in course["enrolled_students"]:
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
                student["grades"][course_id.upper()] = grade_value
                save_data("data/students.json", students)
                print("Grade Added Successfully")
                return

    def edit_grades(self, logged_in_user):
        
        teacher = self.get_teacher_data(logged_in_user)
        students = load_data("data/students.json")
        
        assigned = False
        
        if not teacher:
            print("Teacher not found.")
            return
        
        course_id = input("Enter Course ID: ").strip().upper()
        
        
        for teacher_course in teacher["courses"]:
        
            if teacher_course.upper() == course_id.upper():
                assigned = True
                break
        
        if not assigned:
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
        print("Error: Couldn't edit student grade.")

    def take_attendance(self, logged_in_user):
        teacher = self.get_teacher_data(logged_in_user)
        if not teacher:
            print("Teacher not found.")
            return
        attendance(teacher)
