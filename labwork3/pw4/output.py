def show_menu():
    print("  STUDENT MARK MANAGEMENT SYSTEM")
    print("1. Input students")
    print("2. Input courses")
    print("3. Input marks for a course")
    print("4. List courses")
    print("5. List students & GPA (descending)")
    print("6. Show marks of a course")
    print("7. Exit")


def list_courses(app):
    print("\nCOURSE LIST")
    if not app.get_courses():
        print("No courses yet.")
    else:
        for c in app.get_courses():
            print(c)


def list_students(app):
    print("\nSTUDENT LIST")
    if not app.get_students():
        print("No students yet.")
    else:
        app.sort_students_by_gpa()
        for s in app.get_students():
            print(s)


def show_marks(app, c_id):
    if not app.has_marks(c_id):
        print("No marks for this course yet.")
    else:
        print(f"\nMARKS OF COURSE {c_id}:")
        for s in app.get_students():
            score = app.get_mark(c_id, s.get_id())
            print(f"ID: {s.get_id():<8} | Name: {s.get_name():<20} | Mark: {score}")