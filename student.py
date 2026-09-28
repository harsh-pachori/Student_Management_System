from file_handler import load_students, save_students


def add_student():
    students = load_students()

    student_id = input("Enter student ID: ")

    if student_id in students:
        print("Student ID already exists.")
        return

    name = input("Enter student name: ")
    age = input("Enter age: ")
    course = input("Enter class/course: ")
    phone = input("Enter phone number: ")

    students[student_id] = {
        "name": name,
        "age": age,
        "course": course,
        "phone": phone,
        "marks": {},
        "attendance": 0
    }

    save_students(students)

    print("Student added successfully.")