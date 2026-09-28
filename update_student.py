from file_handler import load_students, save_students


def update_student():
    students = load_students()

    student_id = input("Enter student ID to update: ")

    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]

    print("Press Enter if you want to keep the old value.")

    name = input("Enter new name: ")
    age = input("Enter new age: ")
    course = input("Enter new class/course: ")
    phone = input("Enter new phone number: ")

    if name:
        student["name"] = name

    if age:
        student["age"] = age

    if course:
        student["course"] = course

    if phone:
        student["phone"] = phone

    save_students(students)

    print("Student details updated successfully.")