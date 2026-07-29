
def Admin_menu():
    menu_text = """
===================================
    Admin Management System
===================================
1. Student Management
2. Teacher Management
3. Course Management
4. Department Management
5. Reports
0. Logout
==================================="""
    print(menu_text)

def report_menu():
    menu_text ="""
===================================
           Reports
===================================
1. Student Report
2. Teacher Report
3. Course Report
4. Department Report
0. Back
==================================="""
    print(menu_text)
    

def Student_Management_menu():
    menu_text = """
===================================
    Student Management System
===================================
1. Add Student
2. View all Students
3. Search Student
4. Edit Student data
5. Delete Student
0. Back
==================================="""
    print(menu_text)
def Teacher_Management_menu():
    menu_text = """
===================================
    Teacher Management System
===================================
1. Add Teacher
2. View all Teachers
3. Search Teacher
4. Edit Teacher data
5. Delete Teacher
6. Assign Courses
0. Back
==================================="""
    print(menu_text)

def Course_Management_menu():
    menu_text = """
===================================
    Course Management System
===================================
1. Add Course
2. View all Courses
3. Search Course
4. Edit Course data
5. Delete Course
6. Assign Teacher
7. Register student
0. Back
==================================="""
    print(menu_text)

def Department_Management_menu():
    menu_text = """
===================================
    Department Management System
===================================
1. Add Department
2. View all Department
3. Search Department 
4. Edit Department data
5. Delete Department
6. Assign Head
0. Back
==================================="""
    print(menu_text)

def Teacher_menu():
    menu_text = """
===================================
         Teacher Menu
===================================
1. View Assigned Courses
2. View Students
3. Enter Grades
4. Edit Grades
5. Attendance
0. Logout
==================================="""
    print(menu_text)

def Student_menu():
    menu_text = """
===================================
         Student Menu
===================================
1. View Profile
2. View Courses
3. Register Course
4. Drop Course
5. View Grades
6. View Attendance
0. Logout
==================================="""
    print(menu_text)

def teacher_edit_menu():
    menu_text = """
===================================
        Update Teacher Data
===================================
1. Edit First Name
2. Edit Last Name
3. Edit Password
4. Edit Office
5. Edit Phone
0. Back
==================================="""
    print(menu_text)

def student_edit_menu():
    menu_text = """
===================================
        Update Student Data
===================================
1. Edit First Name
2. Edit Last Name
3. Edit Password
4. Edit Phone
5. Edit Academic Level
0. Back
==================================="""
    print(menu_text)

def course_edit_menu():
    menu_text = """
===================================
        Update Course Data
===================================
1. Edit Course Name
2. Edit Credit hours
3. Edit Assigned Teacher
0. Back
==================================="""
    print(menu_text)

def department_edit_menu():
    menu_text = """
===================================
    Update Department Data
===================================
1. Edit Department Name
2. Edit Building
3. Edit Head of Department
0. Back
==================================="""
    print(menu_text)

def success_message(message):
    print("=" * 35)
    print(message)
    print("=" * 35)
    
def teacher_edit_message():
    print("="*30)
    print("Teacher data Updated Successfully")
    print("="*30)

def student_edit_message():
    print("="*30)
    print("Student data Updated Successfully")
    print("="*30)
def department_edit_message():
    print("="*30)
    print("Student data Updated Successfully")
    print("="*30)