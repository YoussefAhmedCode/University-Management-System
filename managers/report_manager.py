from storage.file_manager import load_data


class ReportManager:

    def student_report(self):

        students = load_data("data/students.json")
        courses = load_data("data/courses.json")

        if not students:
            print("No Students Found.")
            return

        print("=" * 40)
        print("Student Report")
        print("=" * 40)

        for student in students:

            print("Student ID:", student["student_id"])
            print("Name:", student["first_name"], student["last_name"])
            print("Email:", student["email"])
            print("Department:", student["department"])
            print("Academic Level:", student["academic_level"])

            print("Registered Courses:")

            for course_id in student.get("courses", []):
                for course in courses:
                    if course["course_id"] == course_id:
                        print("-", course["course_name"], "(" + course_id + ")")
                        break

            grades = student.get("grades", {})

            if grades:
                print("Grades:")

                for course_id in grades:
                    for course in courses:
                        if course["course_id"] == course_id:
                            print("-", course["course_name"], ":", grades[course_id])
                            break

            print("-" * 40)

    def teacher_report(self):

        teachers = load_data("data/teachers.json")
        courses = load_data("data/courses.json")

        if not teachers:
            print("No Teachers Found.")
            return

        print("=" * 40)
        print("Teacher Report")
        print("=" * 40)

        for teacher in teachers:

            print("Teacher ID:", teacher["teacher_id"])
            print("Name:", teacher["first_name"], teacher["last_name"])
            print("Email:", teacher["email"])
            print("Department:", teacher["department"])
            print("Office:", teacher["office"])

            print("Assigned Courses:")

            for course_id in teacher.get("courses", []):
                for course in courses:
                    if course["course_id"].lower() == course_id.lower():
                        print("-", course["course_name"], "(" + course_id + ")")
                        break

            print("-" * 40)
            
    def course_report(self):

        courses = load_data("data/courses.json")
        teachers = load_data("data/teachers.json")
        students = load_data("data/students.json")

        if not courses:
            print("No Courses Found.")
            return

        print("=" * 40)
        print("Course Report")
        print("=" * 40)

        for course in courses:

            print("Course ID:", course["course_id"])
            print("Course Name:", course["course_name"])
            print("Department:", course["department"])
            print("Credit Hours:", course["credit_hours"])

            print("Teachers:")

            for teacher_id in course.get("teacher_ids", []):
                for teacher in teachers:
                    if teacher["teacher_id"] == teacher_id:
                        print("-", teacher["first_name"], teacher["last_name"])
                        break

            print("Enrolled Students:", len(course["enrolled_students"]))

            for student_id in course.get("enrolled_students", []):
                for student in students:
                    if student["student_id"] == student_id:
                        print("-", student["first_name"], student["last_name"])
                        break

            print("-" * 40)

    def department_report(self):

        departments = load_data("data/departments.json")
        teachers = load_data("data/teachers.json")
        students = load_data("data/students.json")
        courses = load_data("data/courses.json")

        if not departments:
            print("No Departments Found.")
            return

        print("=" * 40)
        print("Department Report")
        print("=" * 40)

        for department in departments:

            print("Department ID:", department["department_id"])
            print("Department Name:", department["name"])
            print("Building:", department["building"])
            print("Head:", department["head_of_department"])

            print("\nTeachers:")

            count = 0

            for teacher in teachers:
                if teacher["department"].lower() == department["name"].lower():
                    print("-", teacher["first_name"], teacher["last_name"])
                    count += 1

            print("Total Teachers:", count)

            print("\nStudents:")

            count = 0

            for student in students:
                if student["department"].lower() == department["name"].lower():
                    print("-", student["first_name"], student["last_name"])
                    count += 1

            print("Total Students:", count)

            print("\nCourses:")

            count = 0

            for course in courses:
                if course["department"].lower() == department["name"].lower():
                    print("-", course["course_name"])
                    count += 1

            print("Total Courses:", count)

            print("-" * 40)