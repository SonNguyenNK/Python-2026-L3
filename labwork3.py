import curses
import math
import numpy as np


class Student:
    def __init__(self, student_id="", name="", dob=""):
        self.__id = student_id
        self.__name = name
        self.__dob = dob
        self.__gpa = 0.0

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def input_info(self, stdscr):
        self.__id = get_input(stdscr, "  Student ID: ")
        self.__name = get_input(stdscr, "  Student name: ")
        self.__dob = get_input(stdscr, "  Date of birth (DoB): ")

    def __str__(self):
        return f"ID: {self.__id:<8} | Name: {self.__name:<20} | DoB: {self.__dob:<12} | GPA: {self.__gpa:.2f}"


class Course:
    def __init__(self, course_id="", name="", credits=0):
        self.__id = course_id
        self.__name = name
        self.__credits = credits

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_credits(self):
        return self.__credits

    def input_info(self, stdscr):
        self.__id = get_input(stdscr, "  Course ID: ")
        self.__name = get_input(stdscr, "  Course name: ")
        self.__credits = int(get_input(stdscr, "  Credits: "))

    def __str__(self):
        return f"Course ID: {self.__id:<8} | Name: {self.__name:<20} | Credits: {self.__credits}"


class StudentMarkManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}  

    def input_students(self, stdscr):
        stdscr.addstr("\nINPUT STUDENTS\n\n")
        count = int(get_input(stdscr, "Number of students: "))

        for i in range(count):
            stdscr.addstr(f"\nStudent {len(self.__students) + 1}:\n")
            s = Student()
            s.input_info(stdscr)
            self.__students.append(s)

        stdscr.addstr("\nStudents added successfully\n")

    def input_courses(self, stdscr):
        stdscr.addstr("\nINPUT COURSES\n\n")
        count = int(get_input(stdscr, "Number of courses: "))

        for i in range(count):
            stdscr.addstr(f"\nCourse {len(self.__courses) + 1}:\n")
            c = Course()
            c.input_info(stdscr)
            self.__courses.append(c)

        stdscr.addstr("\n Courses added successfully\n")

    def input_marks(self, stdscr):
        stdscr.addstr("\nINPUT MARKS\n\n")
        if not self.__courses or not self.__students:
            stdscr.addstr("Please input students and courses first\n")
            return

        c_id = get_input(stdscr, "Enter the course ID to input marks: ")
        course = None
        for c in self.__courses:
            if c.get_id() == c_id:
                course = c

        if course is None:
            stdscr.addstr("Course ID not found!\n")
            return

        self.__marks[c_id] = {}

        stdscr.addstr(f"\nInput marks for: {course.get_name()} (marks are rounded down to 1 decimal place):\n")
        for s in self.__students:
            raw_score = float(get_input(stdscr, f"  Mark for {s.get_name()} (ID: {s.get_id()}): "))
            # Use math.floor() to round down to 1 decimal place
            self.__marks[c_id][s.get_id()] = math.floor(raw_score * 10) / 10.0

        stdscr.addstr("\n Marks input completed\n")

    def calculate_gpas(self):
        for s in self.__students:
            s_id = s.get_id()
            scores_list = []
            credits_list = []

            for c in self.__courses:
                c_id = c.get_id()
                if c_id in self.__marks and s_id in self.__marks[c_id]:
                    scores_list.append(self.__marks[c_id][s_id])
                    credits_list.append(c.get_credits())

            if credits_list:
                np_scores = np.array(scores_list)
                np_credits = np.array(credits_list)

                # sum(scores * credits) / sum(credits)
                weighted_gpa = np.sum(np_scores * np_credits) / np.sum(np_credits)
                s.set_gpa(weighted_gpa)
            else:
                s.set_gpa(0.0)

    def sort_students_by_gpa(self):
        self.calculate_gpas()
        self.__students.sort(key=lambda s: s.get_gpa(), reverse=True)

    def list_students(self, stdscr):
        stdscr.addstr("\nSTUDENT LIST\n\n")
        if not self.__students:
            stdscr.addstr("No students yet.\n")
        else:
            self.sort_students_by_gpa()
            for s in self.__students:
                stdscr.addstr(f"{s}\n")

    def list_courses(self, stdscr):
        stdscr.addstr("\nCOURSE LIST\n\n")
        if not self.__courses:
            stdscr.addstr("No courses yet.\n")
        else:
            for c in self.__courses:
                stdscr.addstr(f"{c}\n")

    def show_marks(self, stdscr):
        stdscr.addstr("\nCOURSE MARKS\n\n")
        c_id = get_input(stdscr, "Enter the course ID to show marks: ")

        if c_id not in self.__marks:
            stdscr.addstr("No marks for this course yet.\n")
        else:
            stdscr.addstr(f"\nMARKS OF COURSE {c_id}:\n")
            for s in self.__students:
                s_id = s.get_id()
                score = self.__marks[c_id].get(s_id, "N/A")
                stdscr.addstr(f"ID: {s_id:<8} | Name: {s.get_name():<20} | Mark: {score}\n")


def get_input(stdscr, prompt):
    stdscr.addstr(prompt)
    stdscr.refresh()
    curses.echo()
    input_bytes = stdscr.getstr()
    curses.noecho()
    return input_bytes.decode('utf-8').strip()


def main(stdscr):
    stdscr.scrollok(True)         # Let the screen scroll when it is full
    curses.curs_set(1)
    app = StudentMarkManagement()

    while True:
        stdscr.addstr("\nSTUDENT MARK MANAGEMENT\n")
        stdscr.addstr("1. Input students\n")
        stdscr.addstr("2. Input courses\n")
        stdscr.addstr("3. Input marks for a course\n")
        stdscr.addstr("4. List courses\n")
        stdscr.addstr("5. List students & GPA\n")
        stdscr.addstr("6. Show marks of a course\n")
        stdscr.addstr("7. Exit\n")

        choice = get_input(stdscr, "Your choice (1-7): ")

        if choice == '1':
            app.input_students(stdscr)
        elif choice == '2':
            app.input_courses(stdscr)
        elif choice == '3':
            app.input_marks(stdscr)
        elif choice == '4':
            app.list_courses(stdscr)
        elif choice == '5':
            app.list_students(stdscr)
        elif choice == '6':
            app.show_marks(stdscr)
        elif choice == '7':
            break


if __name__ == "__main__":
    curses.wrapper(main)