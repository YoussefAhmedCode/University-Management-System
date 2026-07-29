from managers.student_manager import StudentManager
from managers.teacher_manager import TeacherManager
from managers.course_manager import CourseManager
from managers.department_manager import DepartmentManager
from login import login_attempt
import menus


student_manager = StudentManager()
teacher_manager = TeacherManager()
course_manager = CourseManager()
department_manager = DepartmentManager()


while True:
    print("\n" + "="*35)
    print("    UNIVERSITY MANAGEMENT SYSTEM")
    print("="*35)
    
    user = login_attempt()
    role=user["role"]

    if role == "Admin":
        while True:
            menus.Admin_menu()
                       
            choice = input("Enter your Choice (0-5): ")


            if choice == "1":
                while True:
                    menus.Student_Management_menu()
                    sub_choice = input("Choice: ")

                    if sub_choice == "1":
                        student_manager.add_student()
                    elif sub_choice == "2":
                        student_manager.view_all_students()
                    elif sub_choice == "3":
                        student_manager.find_student_by_id()
                    elif sub_choice == "4":
                        student_manager.edit_student_data()
                    elif sub_choice == "5":
                        student_manager.delete_student()
                    elif sub_choice == "0":
                        break
                

            elif choice == "2":
                while True:
                    menus.Teacher_Management_menu()
                    sub_choice = input("Choice: ")

                    if sub_choice == "1":
                        teacher_manager.add_teacher()
                    elif sub_choice == "2":
                        teacher_manager.view_all_teachers()
                    elif sub_choice == "3":
                        teacher_manager.search_teacher()
                    elif sub_choice == "4":
                        teacher_manager.edit_teacher()
                    elif sub_choice == "5":
                        teacher_manager.delete_teacher()
                    elif sub_choice == "6":
                        teacher_manager.assign_course()
                    elif sub_choice == "0":
                        break

            elif choice == "3":
                while True:
                    menus.Course_Management_menu()
                    sub_choice = input("Choice: ")

                    if sub_choice == "1":
                        course_manager.add_course()
                    elif sub_choice == "2":
                        course_manager.view_all_courses()
                    elif sub_choice == "3":
                        course_manager.search_course()
                    elif sub_choice == "4":
                        course_manager.edit_course_data()
                    elif sub_choice == "5":
                        course_manager.delete_course()
                    elif sub_choice == "6":
                        course_manager.assign_teacher()
                    elif sub_choice == "7":
                        course_manager.register_student()
                    elif sub_choice == "0":
                        break
            
            elif choice == "4":
                while True:
                    menus.Department_Management_menu()
                    sub_choice = input("Enter your Choice: ")

                    if sub_choice == "1":
                        department_manager.add_department()
                    elif sub_choice == "2":
                        department_manager.view_departments()
                    elif sub_choice == "3":
                        department_manager.search_department()
                    elif sub_choice == "4":
                        department_manager.edit_department_data()
                    elif sub_choice == "5":
                        department_manager.delete_department()
                    elif sub_choice == "6":
                        department_manager.assign_head()
                    elif sub_choice == "0":
                        break
                    else:
                        print("Invalid Choice.")
                        
            elif choice == "0":
                break

    elif role == "Teacher":
        while True:
            menus.Teacher_menu()
            choice = input(" Enter your Choice (0-5): ")

            if choice == "1":
                teacher_manager.view_assigned_courses(user)
            elif choice == "2":
                teacher_manager.view_enrolled_students(user)
            elif choice == "3":
                teacher_manager.enter_grades(user)
            elif choice == "4":
                teacher_manager.edit_grades(user)
            elif choice == "5":
                teacher_manager.take_attendance(user)
            elif choice == "6":
                teacher_manager.assign_course()
            elif choice == "0":
                print("Logging out...")
                break
            else:
                print("Invalid choice.")

    elif role == "Student":
        while True:
            menus.Student_menu()
            choice = input(" Enter your Choice (0-6): ")

            if choice == "1":
                student_manager.view_profile(user)
            elif choice == "2":
                student_manager.view_courses(user)
            elif choice == "3":
                course_manager.register_course(user)
            elif choice == "4":
                course_manager.drop_course(user)
            elif choice == "5":
                student_manager.view_grades(user)
            elif choice == "6":
                student_manager.view_attendance(user)
            elif choice == "0":
                print("Logging out...")
                break
            else:
                print("Invalid choice.")