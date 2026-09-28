from file_handler import load_students


def calculate_grade():
    students = load_students()

    student_id = input("Enter student ID: ")

    if student_id not in students:
        print("Student not found.")
        return

    marks = students[student_id]["marks"]

    if not marks:
        print("No marks available for this student.")
        return

    total = sum(marks.values())
    percentage = total / len(marks)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    print("\n----- RESULT -----")
    print("Total Marks:", total)
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)