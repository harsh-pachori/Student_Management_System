from student import add_student
from view_student import view_students
from search_student import search_student
from update_student import update_student
from delete_student import delete_student
from marks import add_marks
from attendance import update_attendance
from grades import calculate_grade
from reports import student_report


def main():

    while True:

        print("\n==============================")
        print("    STUDENT MANAGEMENT SYSTEM")
        print("==============================")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Add Marks")
        print("7. Update Attendance")
        print("8. Calculate Grade")
        print("9. Student Report")
        print("10. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            add_marks()

        elif choice == "7":
            update_attendance()

        elif choice == "8":
            calculate_grade()

        elif choice == "9":
            student_report()

        elif choice == "10":
            print("Thank you for using Student Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()