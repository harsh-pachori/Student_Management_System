from file_handler import load_students, save_students


def add_marks():
    students = load_students()

    student_id = input("Enter student ID: ")

    if student_id not in students:
        print("Student not found.")
        return

    subject = input("Enter subject: ")
    
    try:
        marks = float(input("Enter marks: "))

        if marks < 0 or marks > 100:
            print("Marks should be between 0 and 100.")
            return

        students[student_id]["marks"][subject] = marks

        save_students(students)

        print("Marks added successfully.")

    except ValueError:
        print("Please enter valid marks.")