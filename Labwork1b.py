class Student:
    def __init__(self, student_id="", name="", dob=""):
        self.__id = student_id
        self.__name = name
        self.__dob = dob

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def input_info(self):
        self.__id = input("  Student ID: ")  # private attribute
        self.__name = input("  Student name: ")
        self.__dob = input("  Student DoB: ")

    def display(self):
        print(f"ID: {self.__id} | Name: {self.__name} | DoB: {self.__dob}")

    def __str__(self):
        return f"ID: {self.__id} | Name: {self.__name} | DoB: {self.__dob}"


class Course:
    def __init__(self, course_id="", name=""):
        self.__id = course_id
        self.__name = name

    # Getter methods
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def input_info(self):
        self.__id = input("  Course ID: ")
        self.__name = input("  Course name: ")

    def display(self):
        print(f"Course ID: {self.__id} | Course name: {self.__name}")

    def __str__(self):
        return f"Course ID: {self.__id} | Course name: {self.__name}"


class StudentMarkManagement:
    def __init__(self):
        self.__students = []  # List of Student objects
        self.__courses = []   # List of Course objects
        self.__marks = {}     

    def input_students(self):
        count = int(input("Number of students: "))
        for _ in range(count):
            print(f"\nEnter student {len(self.__students) + 1}:")
            s = Student()
            s.input_info()
            self.__students.append(s)

    def input_courses(self):
        count = int(input("Number of courses: "))
        for _ in range(count):
            print(f"\nEnter course {len(self.__courses) + 1}:")
            c = Course()
            c.input_info()
            self.__courses.append(c)

    def list_courses(self):
        print("\nCOURSE LIST")
        if not self.__courses:
            print("No courses yet.")
            return
        for c in self.__courses:
            c.display()

    def list_students(self):
        print("\nSTUDENT LIST")
        if not self.__students:
            print("No students yet.")
            return
        for s in self.__students:
            s.display()

    def input_marks(self):
        if not self.__courses:
            print("No courses yet! Please input courses first.")
            return
        if not self.__students:
            print("No students yet! Please input students first.")
            return

        self.list_courses()
        c_id = input("\nEnter the course ID to input marks: ")

        # Check that the course exists
        course_exists = any(c.get_id() == c_id for c in self.__courses)
        if not course_exists:
            print("Invalid course ID!")
            return

        if c_id not in self.__marks:
            self.__marks[c_id] = {}

        print(f"\nInput marks for course ID: {c_id}")
        for s in self.__students:
            score = float(input(f"Mark for student '{s.get_name()}' (ID: {s.get_id()}): "))
            self.__marks[c_id][s.get_id()] = score

    def show_marks(self):
        if not self.__marks:
            print("No marks have been entered yet.")
            return

        c_id = input("Enter the course ID to show marks: ")
        if c_id not in self.__marks:
            print(f"No marks for course ID: {c_id}")
            return

        print(f"\n--- MARKS OF COURSE: {c_id} ---")
        for s in self.__students:
            s_id = s.get_id()
            score = self.__marks[c_id].get(s_id, "N/A")
            print(f"ID: {s_id} | Name: {s.get_name()} | Mark: {score}")

    def main_menu(self):
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
                self.input_students()
            elif choice == '2':
                self.input_courses()
            elif choice == '3':
                self.input_marks()
            elif choice == '4':
                self.list_courses()
            elif choice == '5':
                self.list_students()
            elif choice == '6':
                self.show_marks()
            elif choice == '7':
                print("Program closed.")
                break
            else:
                print("Invalid choice. Please try again!")


if __name__ == "__main__":
    app = StudentMarkManagement()
    app.main_menu()