from file_handler import load_students, save_students


def delete_student():
    students = load_students()

    student_id = input("Enter student ID to delete: ")

    if student_id not in students:
        print("Student not found.")
        return

    del students[student_id]

    save_students(students)

    print("Student record deleted successfully.")