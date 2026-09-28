from file_handler import load_students, save_students


def update_attendance():
    students = load_students()

    student_id = input("Enter student ID: ")

    if student_id not in students:
        print("Student not found.")
        return

    try:
        attendance = float(input("Enter attendance percentage: "))

        if attendance < 0 or attendance > 100:
            print("Attendance should be between 0 and 100.")
            return

        students[student_id]["attendance"] = attendance

        save_students(students)

        print("Attendance updated successfully.")

    except ValueError:
        print("Please enter a valid percentage.")