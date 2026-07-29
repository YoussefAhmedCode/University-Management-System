# 🎓 University Management System

A console-based **University Management System** built with **Python** using Object-Oriented Programming (OOP) principles and JSON file storage.

The system allows administrators to manage students, teachers, courses, departments, and generate reports, while teachers and students have their own dedicated portals.

---

# 📌 Features

## 👨‍💼 Admin

### Student Management
- Add Student
- View All Students
- Search Student
- Edit Student Information
- Delete Student

### Teacher Management
- Add Teacher
- View All Teachers
- Search Teacher
- Edit Teacher Information
- Delete Teacher
- Assign Courses

### Course Management
- Add Course
- View All Courses
- Search Course
- Edit Course
- Delete Course
- Assign Teachers
- Register Students

### Department Management
- Add Department
- View Departments
- Search Department
- Edit Department
- Delete Department
- Assign Head of Department

### Reports
- Student Report
- Teacher Report
- Course Report
- Department Report

---

## 👨‍🏫 Teacher Portal

Teachers can:

- View Assigned Courses
- View Enrolled Students
- Enter Grades
- Edit Grades
- Take Attendance

---

## 👨‍🎓 Student Portal

Students can:

- View Profile
- View Registered Courses
- Register for Courses
- Drop Courses
- View Grades
- View Attendance

---

# 🗂 Project Structure

```
University-Management-System/
│
├── data/
│   ├── students.json
│   ├── teachers.json
│   ├── courses.json
│   ├── departments.json
│   ├── users.json
│   └── attendance.json
│
├── managers/
│   ├── student_manager.py
│   ├── teacher_manager.py
│   ├── course_manager.py
│   ├── department_manager.py
│   └── report_manager.py
│
├── models/
│   ├── user.py
│   ├── student.py
│   ├── teacher.py
│   ├── course.py
│   └── department.py
│
├── storage/
│   └── file_manager.py
│
├── utils/
│   └── id_generator.py
│
├── menus.py
├── login.py
├── main.py
└── README.md
```

---

# 💾 Data Storage

The project stores all information using JSON files.

- students.json
- teachers.json
- courses.json
- departments.json
- users.json
- attendance.json

No external database is required.

---

# 🛠 Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON File Storage

---

# 🔐 Login System

The system supports three user roles:

- Admin
- Teacher
- Student

Each user logs in using their email and password.

---

# 🔄 Relationships

- A student can register for multiple courses.
- A course can have multiple teachers.
- A teacher can teach multiple courses.
- A department contains students, teachers, and courses.
- Deleting a student, teacher, or course automatically updates all related records.

---

# ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/yourusername/University-Management-System.git
```

Navigate to the project:

```bash
cd University-Management-System
```

Run the application:

```bash
python main.py
```

---

# 📖 Example Workflow

1. Login as Admin.
2. Create Departments.
3. Add Teachers.
4. Add Students.
5. Create Courses.
6. Assign Teachers to Courses.
7. Register Students in Courses.
8. Login as Teacher to manage grades and attendance.
9. Login as Student to view courses, grades, and attendance.

---

# 🚀 Future Improvements

- GPA Calculation
- Semester Management
- Course Prerequisites
- Search Filters
- CSV/PDF Report Export
- SQLite/MySQL Database Support
- Graphical User Interface (Tkinter or PyQt)
- Web Version using Flask or Django

---

# 👨‍💻 Author

Developed as a Python Object-Oriented Programming project.

---

# 📄 License

This project is intended for educational purposes.
