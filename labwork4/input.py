import math

from domains import Student, Course


def input_students(app):
    print("\nINPUT STUDENTS")
    count = int(input("Number of students: "))

    for i in range(count):
        print(f"\nStudent {len(app.get_students()) + 1}:")
        s_id = input("  Student ID: ")
        name = input("  Student name: ")
        dob = input("  Date of birth (DoB): ")
        app.add_student(Student(s_id, name, dob))

    print(" Students added successfully")


def input_courses(app):
    print("\n INPUT COURSES ")
    count = int(input("Number of courses: "))

    for i in range(count):
        print(f"\nCourse {len(app.get_courses()) + 1}:")
        c_id = input("  Course ID: ")
        name = input("  Course name: ")
        credits = int(input("  Credits: "))
        app.add_course(Course(c_id, name, credits))

    print(" Courses added successfully")


def input_marks(app):
    print("\n INPUT MARKS ")
    if not app.get_courses() or not app.get_students():
        print("Please input students and courses first")
        return

    c_id = input("Enter the course ID to input marks: ")
    course = app.find_course(c_id)

    if course is None:
        print("Course ID not found")
        return

    app.reset_marks(c_id)

    print(f"\nInput marks for: {course.get_name()} (marks are rounded down to 1 decimal place)")
    for s in app.get_students():
        raw_score = float(input(f"  Mark for {s.get_name()} (ID: {s.get_id()}): "))
        # Use math.floor() to round down to 1 decimal place
        app.set_mark(c_id, s.get_id(), math.floor(raw_score * 10) / 10)

    print(" Marks input completed")


def input_course_id():
    print("\n COURSE MARKS ")
    return input("Enter the course ID to show marks: ")