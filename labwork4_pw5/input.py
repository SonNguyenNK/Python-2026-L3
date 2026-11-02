import math

from domains import Student, Course

def write_students(app):
    with open("students.txt", "w", encoding="utf-8") as f:
        for s in app.get_students():
            f.write(f"{s.get_id()},{s.get_name()},{s.get_dob()}\n")


def write_courses(app):
    with open("courses.txt", "w", encoding="utf-8") as f:
        for c in app.get_courses():
            f.write(f"{c.get_id()},{c.get_name()},{c.get_credits()}\n")


def write_marks(app):
    with open("marks.txt", "w", encoding="utf-8") as f:
        marks = app.get_all_marks()
        for c_id in marks:
            for s_id in marks[c_id]:
                f.write(f"{c_id},{s_id},{marks[c_id][s_id]}\n")


def input_students(app):
    print("\n INPUT STUDENTS ")
    count = int(input("Number of students: "))

    for i in range(count):
        print(f"\nStudent {len(app.get_students()) + 1}:")
        s_id = input("  Student ID: ")
        name = input("  Student name: ")
        dob = input("  Date of birth (DoB): ")
        app.add_student(Student(s_id, name, dob))

    write_students(app)   # write to students.txt
    print("-> Students added successfully!")


def input_courses(app):
    print("\n INPUT COURSES ")
    count = int(input("Number of courses: "))

    for i in range(count):
        print(f"\nCourse {len(app.get_courses()) + 1}:")
        c_id = input("  Course ID: ")
        name = input("  Course name: ")
        credits = int(input("  Credits: "))
        app.add_course(Course(c_id, name, credits))

    write_courses(app)    # write to courses.txt
    print("-> Courses added successfully!")


def input_marks(app):
    print("\n INPUT MARKS ")
    if not app.get_courses() or not app.get_students():
        print("Please input students and courses first!")
        return

    c_id = input("Enter the course ID to input marks: ")
    course = app.find_course(c_id)

    if course is None:
        print("Course ID not found!")
        return

    app.reset_marks(c_id)

    print(f"\nInput marks for: {course.get_name()} (marks are rounded down to 1 decimal place)")
    for s in app.get_students():
        raw_score = float(input(f"  Mark for {s.get_name()} (ID: {s.get_id()}): "))
        # Use math.floor() to round down to 1 decimal place
        app.set_mark(c_id, s.get_id(), math.floor(raw_score * 10) / 10)

    write_marks(app)      # write to marks.txt
    print("-> Marks input completed!")


def input_course_id():
    print("\n COURSE MARKS ")
    return input("Enter the course ID to show marks: ")