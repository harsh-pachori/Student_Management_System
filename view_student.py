from file_handler import load_students


def view_students():
    students = load_students()

    if not students:
        print("No student records found.")
        return

    print("\n----- STUDENT RECORDS -----")

    for student_id, student in students.items():
        print("ID:", student_id)
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Class/Course:", student["course"])
        print("Phone:", student["phone"])
        print("--------------------------")