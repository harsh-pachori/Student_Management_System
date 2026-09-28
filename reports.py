from file_handler import load_students


def student_report():
    students = load_students()

    student_id = input("Enter student ID: ")

    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]

    print("\n==============================")
    print("       STUDENT REPORT")
    print("==============================")

    print("Student ID:", student_id)
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Class/Course:", student["course"])
    print("Phone:", student["phone"])

    print("\nMarks:")

    if student["marks"]:
        total = sum(student["marks"].values())
        percentage = total / len(student["marks"])

        for subject, marks in student["marks"].items():
            print(subject, ":", marks)

        print("Total:", total)
        print("Percentage:", round(percentage, 2), "%")
    else:
        print("No marks available.")

    print("\nAttendance:", student["attendance"], "%")

    print("==============================")