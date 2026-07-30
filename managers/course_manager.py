from storage.file_manager import load_data, save_data
from models.course import Course
from menus import course_edit_menu


class CourseManager:

    def __init__(self):
        pass

    def add_course(self):

        courses = load_data("data/courses.json")

        while True:

            course_id = input("Enter Course ID: ").strip().upper()

            if course_id == "":
                print("Course ID cannot be empty.")
                continue

            found = False

            for course in courses:
                if course["course_id"].upper() == course_id.upper():
                    found = True
                    break

            if found:
                print("Course ID already exists.")
                continue

            break

        course_name = input("Enter Course Name: ").strip()
        departments_data = load_data("data/departments.json")

        while True:
            department_input = input("Enter Department: ").strip().title()
            found_dept = False

            for dept in departments_data:
                if dept["name"].title() == department_input.title():
                    found_dept = True
                    department = dept["name"].title()
                    break

            if found_dept:
                break
            else:
                print(
                    "Error: Department",
                    department_input,
                    "does not exist. Please enter a valid department.",
                )

        while True:

            try:
                credit_hours = int(input("Enter Credit Hours: "))

                if credit_hours <= 0 or credit_hours>4 :
                    print("Credit hours must be greater than zero and less than 5.")
                    continue

                break

            except ValueError:
                print("Invalid Input.")

        new_course = Course(course_id, course_name, department, credit_hours)

        courses.append(new_course.to_dict())
        save_data("data/courses.json", courses)

        print("\nCourse Added Successfully.\n")

    def view_all_courses(self):

        courses = load_data("data/courses.json")

        if not courses:
            print("No Courses Found.")
            return

        print("\n========== Courses ==========\n")

        for course in courses:

            print("Course ID      :", course["course_id"])
            print("Course Name    :", course["course_name"])
            print("Department     :", course["department"])
            print("Credit Hours   :", course["credit_hours"])
            print("Teachers       :", course["teacher_ids"])
            print("Number of Students       :", len(course["enrolled_students"]))

            print("-" * 40)

    def search_course(self):

        courses = load_data("data/courses.json")

        if not courses:
            print("No Courses Found.")
            return

        course_id = input("Enter Course ID: ").strip().upper()

        for course in courses:

            if course["course_id"].upper() == course_id.upper():

                print("\n===== Course Found =====\n")
                print("Course ID      :", course["course_id"])
                print("Course Name    :", course["course_name"])
                print("Department     :", course["department"])
                print("Credit Hours   :", course["credit_hours"])
                print("Teachers       :", course["teacher_ids"])
                print("Students       :", len(course["enrolled_students"]))

                return

        print("Course Not Found.")

    def edit_course_data(self):

        courses = load_data("data/courses.json")
        teachers = load_data("data/teachers.json")

        if not courses:
            print("\nNo Courses Found.\n")
            return

        course_id = input("Enter Course ID to Update: ").strip().upper()

        for course in courses:

            if course["course_id"].upper() == course_id.upper():
                while True:
                    course_edit_menu()
                    choice = input("Enter your Choice (0-4): ")

                    if choice == "1":
                        course_name = input("New Course Name: ").strip()
                        course["course_name"] = course_name

                    elif choice == "2":
                        try:
                            credit_hours = int(input("New Credit Hours: "))
                            if credit_hours <= 0 or credit_hours>4 :
                                print("Credit hours must be greater than zero and less than 5.")
                                continue
                            course["credit_hours"] = credit_hours
                        except ValueError:
                            print("Invalid input.")

                    elif choice == "3":

                        try:
                            old_teacher_id = int(input("Enter Old Teacher ID: "))
                            new_teacher_id = int(input("Enter New Teacher ID: "))
                        except ValueError:
                            print("Invalid Teacher ID.")
                            continue

                        new_teacher = None
                        for teacher in teachers:
                            if teacher["teacher_id"] == new_teacher_id:
                                new_teacher = teacher
                                break

                        if not new_teacher:
                            print("New Teacher Not Found.")
                            continue

                        if new_teacher["department"].title() != course["department"].title():
                            print("Teacher and Course Departments Do Not Match.")
                            continue

                        old_teacher_found = False
                        for i in range(len(course["teacher_ids"])):
                            if course["teacher_ids"][i] == old_teacher_id:
                                course["teacher_ids"][i] = new_teacher_id
                                old_teacher_found = True
                                break

                        if not old_teacher_found:
                            if course["teacher_ids"]:
                                print("Old Teacher Is Not Assigned To This Course.")
                                continue
                            course["teacher_ids"].append(new_teacher_id)

                        for teacher in teachers:
                            if teacher["teacher_id"] == old_teacher_id:
                                if course_id in teacher.get("courses", []):
                                    teacher["courses"].remove(course_id)

                            if teacher["teacher_id"] == new_teacher_id:
                                if course_id not in teacher["courses"]:
                                    teacher["courses"].append(course_id)

                        save_data("data/teachers.json", teachers)
                        save_data("data/courses.json", courses)

                        print("Teacher Updated Successfully.")

                    elif choice == "0":
                        break

                    else:
                        print("Invalid choice.")
                        continue

                save_data("data/courses.json", courses)
                print("\nCourse Updated Successfully.\n")
                return

        print("\nCourse Not Found.\n")

    def delete_course(self):

        courses = load_data("data/courses.json")
        teachers = load_data("data/teachers.json")
        students = load_data("data/students.json")
        
        if not courses:
            print("\nNo Courses Found.\n")
            return
        
        course_id = input("Enter Course ID to Delete: ").strip().upper()
        
        for course in courses:
            
            if course["course_id"].upper() == course_id.upper():
                confirm = input("Are you sure? (Y/N): ").strip().lower()
                
                if confirm == "y":
                    for teacher in teachers:
                        if course_id in teacher["courses"]:
                            teacher["courses"].remove(course_id)
                            
                            
                    save_data("data/teachers.json", teachers)
                    
                    for student in students:
                        if course_id in student["courses"]:
                            student["courses"].remove(course_id)
                            
                            
                    save_data("data/students.json", students)
                    courses.remove(course)
                    save_data("data/courses.json", courses)
                    print("\nCourse Deleted Successfully.\n")
                    return
                    
                else:
                    print("\nDelete Cancelled.\n")
                return
            
        print("\nCourse Not Found.\n")

    def assign_teacher(self):

        courses = load_data("data/courses.json")
        teachers = load_data("data/teachers.json")

        course_id = input("Enter Course ID: ").strip().upper()

        try:
            teacher_id = int(input("Enter Teacher ID: "))
        except ValueError:
            print("Invalid Teacher ID.")
            return

        found_course = False
        found_teacher = False

        for course in courses:

            if course["course_id"].upper() == course_id.upper():

                found_course = True

                for teacher in teachers:

                    if teacher["teacher_id"] == teacher_id:

                        found_teacher = True

                        if teacher["department"].title() != course["department"].title():
                            print("Teacher and Course Departments Do Not Match.")
                            return

                        if teacher_id in course["teacher_ids"]:
                            print("Teacher Already Assigned To This Course.")
                            return

                        course["teacher_ids"].append(teacher_id)

                        if course_id not in teacher["courses"]:
                            teacher["courses"].append(course_id)

                        save_data("data/courses.json", courses)
                        save_data("data/teachers.json", teachers)

                        print("Teacher Assigned Successfully.")
                        return

        if not found_course:
            print("Course Not Found.")
        elif not found_teacher:
            print("Teacher Not Found.")

    def register_student(self):
        courses = load_data("data/courses.json")
        students = load_data("data/students.json")

        found_course = False

        course_id = input("Enter course ID: ").upper()
        print("-" * 20)

        for course in courses:
            if course["course_id"].upper() == course_id.upper():
                found_course = True

                while True:
                    print("Press Enter if you finished.")
                    student_id = input("Enter Student ID: ")

                    if student_id == "":
                        break

                    try:
                        student_id = int(student_id)
                    except ValueError:
                        print("Invalid input.")
                        continue

                    found_student = False

                    for student in students:
                        if student["student_id"] == student_id:
                            found_student = True

                            if course_id not in student["courses"]:
                                student["courses"].append(course_id)
                                course["enrolled_students"].append(student_id)
                                print("Course registered successfully.")
                            else:
                                print("Course already registered")

                            break

                    if not found_student:
                        print("Student ID doesn't exist.")

                break

        if not found_course:
            print("Course not found.")

        save_data("data/students.json", students)
        save_data("data/courses.json", courses)

    def register_course(self, logged_in_user):
        
        courses = load_data("data/courses.json")
        students = load_data("data/students.json")

        found_course = False
        student_record = None
        for student in students:
            if student["email"] == logged_in_user["email"]:
                student_record = student
                break

        if not student_record:
            print("Student record not found.")
            return

        course_id = input("Enter course ID: ").strip().upper()
        print("-" * 20)

        for course in courses:
            if course["course_id"].upper() == course_id.upper():
                found_course = True

                already_registered = False
                for c in student_record["courses"]:
                    if c.upper() == course_id.upper():
                        already_registered = True
                        break

                if not already_registered:
                    student_record["courses"].append(course["course_id"])
                    course["enrolled_students"].append(student_record["student_id"])
                    print("Course registered successfully.")
                else:
                    print("Course already registered")

                break

        if not found_course:
            print("Course not found.")

        save_data("data/students.json", students)
        save_data("data/courses.json", courses)

    def drop_course(self, logged_in_user):

        courses = load_data("data/courses.json")
        students = load_data("data/students.json")
        attendance = load_data("data/attendance.json")

        found_course = False
        student_record = None

        for student in students:

            if student["email"] == logged_in_user["email"]:
                student_record = student
                break

        if not student_record:
            print("Student Not Found.")
            return

        course_id = input("Enter Course ID: ").strip().upper()

        print("-" * 20)

        for course in courses:

            if course["course_id"].upper() == course_id.upper():

                found_course = True

                target_course = None

                for c in student_record["courses"]:

                    if c == course_id:
                        target_course = c
                        break

                if target_course:

                    student_record["courses"].remove(target_course)

                    if student_record["student_id"] in course["enrolled_students"]:
                        course["enrolled_students"].remove(student_record["student_id"])

                    if "grades" in student_record:

                        if course_id in student_record["grades"]:
                            del student_record["grades"][course_id]

                    attendance_new = []

                    for record in attendance:

                        if record["student_id"] == student_record["student_id"] and record["course_id"] == course_id:
                            continue

                        attendance_new.append(record)

                    attendance = attendance_new

                    print("Course Dropped Successfully.")

                else:
                    print("You Didn't Register This Course.")

                break

        if not found_course:
            print("Course Not Found.")

        save_data("data/students.json", students)
        save_data("data/courses.json", courses)
        save_data("data/attendance.json", attendance)
