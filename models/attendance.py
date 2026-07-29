from storage.file_manager import load_data,save_data

def attendance(logged_in_teacher):
    
        courses = load_data("data/courses.json")
        attendance_data = load_data("data/attendance.json")
        
        course_id = input("Enter Course ID: ").strip().upper()

        teacher_courses = logged_in_teacher["courses"]
        is_assigned = False
        for course in teacher_courses:
            if course.upper() == course_id.upper():
                is_assigned = True
                break

        if not is_assigned:
            print("You are not assigned to this course.")
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

        status = input("Present / Absent: ").strip().capitalize()

        attendance_data.append(
            {"student_id": student_id, "course_id": course_id, "status": status}
        )
        save_data("data/attendance.json", attendance_data)
        print("Attendance Saved Successfully")