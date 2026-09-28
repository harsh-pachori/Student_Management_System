# Student Management System

## About the Project

The Student Management System is a simple Python-based project developed to manage student records in an organized way. It provides basic features such as adding students, viewing records, searching, updating and deleting information.

The system also allows the user to manage marks and attendance, calculate grades, and generate a student report.

## Features

- Add new student
- View all students
- Search for a student
- Update student details
- Delete student records
- Add and manage marks
- Update attendance
- Calculate percentage and grade
- Generate student report
- Save student data using file handling

## Technologies Used

- Python
- JSON
- File Handling
- VS Code

## Project Structure

```text
Student_Management_System/
│
├── main.py
├── student.py
├── view_students.py
├── search_student.py
├── update_student.py
├── delete_student.py
├── marks.py
├── attendance.py
├── grades.py
├── reports.py
├── file_handler.py
├── students.json
└── README.md
```

## How to Run

1. Download or clone the project.
2. Open the project folder in VS Code.
3. Make sure Python is installed on the computer.
4. Open the terminal in the project folder.
5. Run the following command:

```text
python main.py
```

6. The Student Management System menu will appear.
7. Select the required option by entering its number.

## Main Menu

```
==============================
    STUDENT MANAGEMENT SYSTEM
==============================

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Add Marks
7. Update Attendance
8. Calculate Grade
9. Student Report
10. Exit
```

## Data Storage

Student records are stored in a JSON file named `students.json`. The file is automatically created when student information is saved for the first time.

## Project Purpose

The purpose of this project is to demonstrate the practical use of Python programming concepts such as functions, conditional statements, loops, dictionaries, file handling, and modular programming.

## Future Improvements

Some features that can be added in the future are:

- Login system
- More detailed attendance tracking
- Database connectivity
- Graphical user interface
- Exporting student reports
- Different user roles for teachers and administrators

## Author

Harsh Pachori