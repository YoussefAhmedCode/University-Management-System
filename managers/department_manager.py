from storage.file_manager import load_data, save_data
from models.department import Department
from menus import department_edit_message, department_edit_menu


class DepartmentManager:

    def add_department(self):

        departments = load_data("data/departments.json")

        department_id = input("Enter Department ID: ").upper()
        department_name = input("Enter Department Name: ").title()
        building = input("Enter Building: ")

        department = Department(department_id, department_name, building, head_of_department="None")
        new_department = department.to_dict()

        departments.append(new_department)
        save_data("data/departments.json", departments)
        print("Department Added Successfully")

    def view_departments(self):
        
        departments = load_data("data/departments.json")
        if len(departments) == 0:
            print("No Departments Found")
            return
        for department in departments:
            print("-" * 40)
            for key, value in department.items():
                print(key, ":", value)

    def search_department(self):
        
        departments = load_data("data/departments.json")
        department_id = input("Enter Department ID: ").upper()
        
        for department in departments:
            if department["department_id"].upper() == department_id.upper():
                print("=" * 40)
                for key, value in department.items():
                    print(key, ":", value)
                return
        print("Department Not Found")

    def edit_department_data(self):

        departments = load_data("data/departments.json")
        teachers = load_data("data/teachers.json")
        students = load_data("data/students.json")
        courses = load_data("data/courses.json")

        department_id = input("Enter Department ID To Update: ").upper

        found = False

        for department in departments:

            if department["department_id"].upper() == department_id.upper():

                found = True

                while True:

                    department_edit_menu()
                    choice = input("Enter Your Choice: ")

                    if choice == "1":

                        old_name = department["name"]
                        new_name = input("Enter New Department Name: ").title()

                        department["name"] = new_name

                        for teacher in teachers:

                            if teacher["department"] == old_name:
                                teacher["department"] = new_name

                        for student in students:

                            if student["department"] == old_name:
                                student["department"] = new_name

                        for course in courses:

                            if course["department"] == old_name:
                                course["department"] = new_name

                        save_data("data/teachers.json", teachers)
                        save_data("data/students.json", students)
                        save_data("data/courses.json", courses)

                        department_edit_message()

                    elif choice == "2":

                        department["building"] = input("Enter New Building: ")
                        department_edit_message()

                    elif choice == "3":

                        try:
                            teacher_id = int(input("Enter Teacher ID: "))
                        except ValueError:
                            print("Invalid Teacher ID.")
                            continue

                        found_teacher = False

                        for teacher in teachers:

                            if teacher["teacher_id"] == teacher_id:

                                if teacher["department"].title() != department["name"].title():

                                    print("Teacher Does Not Belong To This Department.")
                                    found_teacher = True
                                    break

                                department["head_of_department"] = (
                                    teacher["first_name"] + " " + teacher["last_name"]
                                )

                                department_edit_message()

                                found_teacher = True
                                break

                        if not found_teacher:
                            print("Teacher Not Found.")

                    elif choice == "0":
                        break

                    else:
                        print("Invalid Choice.")

                save_data("data/departments.json", departments)
                return

        if not found:

            print("=" * 30)
            print("Department Not Found")
            print("=" * 30)

    def delete_department(self):

        departments = load_data("data/departments.json")
        teachers = load_data("data/teachers.json")
        students = load_data("data/students.json")
        courses = load_data("data/courses.json")

        department_id = input("Enter Department ID: ").upper()

        for department in departments:

            if department["department_id"].upper() == department_id.upper():

                for teacher in teachers:

                    if teacher["department"].title() == department["name"].title():
                        print("Cannot Delete Department. Teachers Are Assigned.")
                        return

                for student in students:

                    if student["department"].title() == department["name"].title():
                        print("Cannot Delete Department. Students Are Assigned.")
                        return

                for course in courses:

                    if course["department"].title() == department["name"].title():
                        print("Cannot Delete Department. Courses Are Assigned.")
                        return

                confirm = input("Are You Sure? (Y/N): ").strip().lower()

                if confirm == "y":

                    departments.remove(department)
                    save_data("data/departments.json", departments)

                    print("Department Deleted Successfully.")

                else:

                    print("Delete Cancelled.")

                return

        print("Department Not Found")

    def assign_head(self):

        departments = load_data("data/departments.json")
        teachers = load_data("data/teachers.json")

        department_id = input("Enter Department ID: ").upper()

        for department in departments:
            if department["department_id"].upper() == department_id.upper():
                try:
                    teacher_id = int(input("Enter Teacher ID for New Head: "))
                except ValueError:
                    print("Invalid Teacher ID .")
                    return

                for teacher in teachers:
                    if teacher["teacher_id"] == teacher_id:

                        if teacher["department"].title() == department["name"].title():
                            department["head_of_department"] = (
                                teacher["first_name"] + " " + teacher["last_name"]
                            )
                            save_data("data/departments.json", departments)
                            print("Head Assigned Successfully")
                            return
                        else:
                            print("Error: Teacher",teacher["first_name"],"belongs to",teacher["department"],"not",department["name"],)
                            return

                print("Teacher Not Found.")
                return

        print("Department Not Found")
