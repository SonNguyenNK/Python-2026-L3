import os
import zipfile

import output
from domains import Student, Course, StudentMarkManagement
from input import (input_students, input_courses,
                   input_marks, input_course_id)

DATA_FILE = "students.dat"
TEXT_FILES = ["students.txt", "courses.txt", "marks.txt"]


def compress_data():
    with zipfile.ZipFile(DATA_FILE, "w", zipfile.ZIP_DEFLATED) as zf:
        for name in TEXT_FILES:
            if os.path.exists(name):
                zf.write(name)
    print(f"Data compressed into {DATA_FILE}")


def load_data(app):
    if not os.path.exists(DATA_FILE):
        return

    with zipfile.ZipFile(DATA_FILE, "r") as zf:
        zf.extractall()

    if os.path.exists("students.txt"):
        with open("students.txt", "r", encoding="utf-8") as f:
            for line in f:
                s_id, name, dob = line.strip().split(",")
                app.add_student(Student(s_id, name, dob))

    if os.path.exists("courses.txt"):
        with open("courses.txt", "r", encoding="utf-8") as f:
            for line in f:
                c_id, name, credits = line.strip().split(",")
                app.add_course(Course(c_id, name, int(credits)))

    if os.path.exists("marks.txt"):
        with open("marks.txt", "r", encoding="utf-8") as f:
            for line in f:
                c_id, s_id, score = line.strip().split(",")
                app.set_mark(c_id, s_id, float(score))

    print(f"Data loaded from {DATA_FILE}")


def main():
    app = StudentMarkManagement()
    load_data(app)

    while True:
        output.show_menu()
        choice = input("Your choice (1-7): ")

        if choice == '1':
            input_students(app)
        elif choice == '2':
            input_courses(app)
        elif choice == '3':
            input_marks(app)
        elif choice == '4':
            output.list_courses(app)
        elif choice == '5':
            output.list_students(app)
        elif choice == '6':
            c_id = input_course_id()
            output.show_marks(app, c_id)
        elif choice == '7':
            compress_data()
            print("Program closed.")
            break


if __name__ == "__main__":
    main()