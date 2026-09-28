from file_handler import load_students


def search_student():
    students = load_students()

    student_id = input("Enter student ID to search: ")

    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]

    print("\n----- STUDENT DETAILS -----")
    print("ID:", student_id)
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Class/Course:", student["course"])
    print("Phone:", student["phone"])