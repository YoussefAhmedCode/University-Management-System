from storage.file_manager import load_data,save_data 
from models.department import Department
from menus import department_edit_message,department_edit_menu


class DepartmentManager:
    


    def add_department(self):

        departments = load_data("data/departments.json") 

        department_id = input("Enter Department ID: ")
        department_name = input("Enter Department Name: ")
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
                print(key,":", value)


    def search_department(self):
        departments = load_data("data/departments.json")
        department_id = input("Enter Department ID: ")
        for department in departments:
            if department["department_id"] == department_id:
                print("=" * 40)
                for key, value in department.items():
                    print(key, ":", value)
                return
        print("Department Not Found")


    def edit_department_data(self):
        departments = load_data("data/departments.json")
        try:
            department_id = input("Enter Department ID to update: ")
            found = False
            
            for department in departments:
                if department["department_id"] == department_id:
                    found = True
                    while True:
                        department_edit_menu()
                        choice = input("Enter Your choice: ")
                        
                        if choice == "1":
                            department["name"] = input("Enter New Department Name: ").capitalize()
                            department_edit_message()
                        elif choice == "2":
                            department["building"] = input("Enter New Building: ")
                            department_edit_message()
                        elif choice == "3":
                            department["head_of_department"] = input("Enter New Head of Department: ")
                            department_edit_message()
                        elif choice == "0":
                            break
                        else:
                            print("Invalid choice.")
                            continue
                            
            save_data("data/departments.json", departments)
            
            if not found:
                print("=" * 30)
                print("Department Not Found")
                print("=" * 30)
                
        except ValueError:
            print("Invalid input.")


    def delete_department(self):
        departments = load_data("data/departments.json")
        department_id =input("Enter Department ID: ")
        for department in departments:
            if department["department_id"] == department_id:
                departments.remove(department)
                save_data("data/departments.json", departments)
                print("Department Deleted Successfully")
                return
        print("Department Not Found")


    def assign_head(self):

        departments = load_data("data/departments.json")
        teachers = load_data("data/teachers.json")
        
        department_id = input("Enter Department ID: ")
        
        for department in departments:
            if department["department_id"] == department_id:
                try:
                    teacher_id = int(input("Enter Teacher ID for New Head: "))
                except ValueError:
                    print("Invalid Teacher ID .")
                    return

                for teacher in teachers:
                    if teacher["teacher_id"] == teacher_id:

                        if teacher["department"].lower() == department["name"].lower():
                            department["head_of_department"] = teacher["first_name"] + " " + teacher["last_name"]
                            save_data("data/departments.json", departments)
                            print("Head Assigned Successfully")
                            return
                        else:
                            print("Error: Teacher", teacher['first_name'], "belongs to", teacher['department'], "not", department['name'])
                            return
                            
                print("Teacher Not Found.")
                return
                
        print("Department Not Found")