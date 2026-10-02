students = []  
courses = []   
marks = {}     


def input_students():
    count = int(input("Number of students: "))
    for _ in range(count):
        s_id = input("  ID: ")
        name = input("  Name: ")
        dob = input("  DoB: ")
        students.append((s_id, name, dob))


def input_courses():
    count = int(input("Number of courses: "))
    for _ in range(count):
        c_id = input("  Course ID: ")
        name = input("  Course name: ")
        courses.append((c_id, name))


def input_marks():
    list_courses()
    c_id = input("\nEnter the course ID to input marks: ")
    marks[c_id] = {}
    print(f"\nInput marks for course ID: {c_id}")
    for s_id, name, _ in students:
        score = float(input(f"Mark for student '{name}' (ID: {s_id}): "))
        marks[c_id][s_id] = score


def list_courses():
    print("\nCOURSE LIST")
    for c_id, name in courses:
        print(f"Course ID: {c_id} | Course name: {name}")


def list_students():
    print("\nSTUDENT LIST")
    for s_id, name, dob in students:
        print(f"ID: {s_id} | Name: {name} | DoB: {dob}")


def show_marks():
    c_id = input("Enter the course ID to show marks: ")
    print(f"\nMARKS OF COURSE: {c_id}")
    for s_id, name, _ in students:
        score = marks[c_id].get(s_id, "N/A")
        print(f"ID: {s_id} | Name: {name} | Mark: {score}")


def main():
    while True:
        print("\nMANAGEMENT MENU")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List courses")
        print("5. List students")
        print("6. Show marks of a course")
        print("7. Exit")

        choice = input("Your choice (1-7): ")

        if choice == '1':
            input_students()
        elif choice == '2':
            input_courses()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            list_courses()
        elif choice == '5':
            list_students()
        elif choice == '6':
            show_marks()
        elif choice == '7':
            print("Program closed.")
            break


if __name__ == "__main__":
    main()