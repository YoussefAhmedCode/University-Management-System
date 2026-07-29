from storage.file_manager import load_data


def generate_student_id():
    students = load_data("data/students.json")

    if not students:
        return 2600001

    max_id = max(student["student_id"] for student in students)
    return max_id + 1

def generate_teacher_id():
    teachers = load_data("data/teachers.json")

    if not teachers:
        return 1001

    max_id = max(teacher["teacher_id"] for teacher in teachers)
    return max_id + 1
