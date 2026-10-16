import output
from domains import StudentMarkManagement
from input import (input_students, input_courses,
                   input_marks, input_course_id)


def main():
    app = StudentMarkManagement()

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
            print("Program closed.")
            break


if __name__ == "__main__":
    main()