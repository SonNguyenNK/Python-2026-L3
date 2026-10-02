import curses
import math
import numpy as np


class Student:
    """Lop dai dien cho Sinh vien"""
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
        self.__id = get_input(stdscr, "  ID Sinh vien: ")
        self.__name = get_input(stdscr, "  Ten Sinh vien: ")
        self.__dob = get_input(stdscr, "  Ngay sinh (DoB): ")

    def __str__(self):
        return f"ID: {self.__id:<8} | Ten: {self.__name:<20} | DoB: {self.__dob:<12} | GPA: {self.__gpa:.2f}"


class Course:
    """Lop dai dien cho Mon hoc"""
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
        self.__id = get_input(stdscr, "  ID Mon hoc: ")
        self.__name = get_input(stdscr, "  Ten Mon hoc: ")
        self.__credits = int(get_input(stdscr, "  So tin chi (credits): "))

    def __str__(self):
        return f"ID Mon: {self.__id:<8} | Ten Mon: {self.__name:<20} | Tin chi: {self.__credits}"


class StudentMarkManagement:
    """Lop Quan ly He thong bang Curses"""
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}  # Cau truc: {course_id: {student_id: score}}

    def input_students(self, stdscr):
        stdscr.addstr("\n=== NHAP THONG TIN SINH VIEN ===\n\n")
        count = int(get_input(stdscr, "Nhap so luong sinh vien: "))

        for i in range(count):
            stdscr.addstr(f"\nSinh vien thu {len(self.__students) + 1}:\n")
            s = Student()
            s.input_info(stdscr)
            self.__students.append(s)

        stdscr.addstr("\n-> Da them sinh vien thanh cong!\n")

    def input_courses(self, stdscr):
        stdscr.addstr("\n=== NHAP THONG TIN MON HOC ===\n\n")
        count = int(get_input(stdscr, "Nhap so luong mon hoc: "))

        for i in range(count):
            stdscr.addstr(f"\nMon hoc thu {len(self.__courses) + 1}:\n")
            c = Course()
            c.input_info(stdscr)
            self.__courses.append(c)

        stdscr.addstr("\n-> Da them mon hoc thanh cong!\n")

    def input_marks(self, stdscr):
        stdscr.addstr("\n=== NHAP DIEM MON HOC ===\n\n")
        if not self.__courses or not self.__students:
            stdscr.addstr("Can phai nhap danh sach Mon hoc va Sinh vien truoc!\n")
            return

        c_id = get_input(stdscr, "Nhap ID mon hoc de nhap diem: ")
        course = None
        for c in self.__courses:
            if c.get_id() == c_id:
                course = c

        if course is None:
            stdscr.addstr("Khong tim thay ID mon hoc nay!\n")
            return

        self.__marks[c_id] = {}

        stdscr.addstr(f"\nNhap diem cho mon: {course.get_name()} (Diem se duoc lam tron xuong 1 chu so thap phan):\n")
        for s in self.__students:
            raw_score = float(get_input(stdscr, f"  Diem cho {s.get_name()} (ID: {s.get_id()}): "))
            # Dung math.floor() lam tron xuong 1 chu so thap phan
            self.__marks[c_id][s.get_id()] = math.floor(raw_score * 10) / 10.0

        stdscr.addstr("\n-> Nhap diem hoan tat!\n")

    def calculate_gpas(self):
        """Tinh diem GPA trung binh co trong so bang mang NumPy"""
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
        """Sap xep sinh vien theo GPA giam dan"""
        self.calculate_gpas()
        self.__students.sort(key=lambda s: s.get_gpa(), reverse=True)

    def list_students(self, stdscr):
        stdscr.addstr("\n=== DANH SACH SINH VIEN (SAP XEP THEO GPA GIAM DAN) ===\n\n")
        if not self.__students:
            stdscr.addstr("Chua co sinh vien nao.\n")
        else:
            self.sort_students_by_gpa()
            for s in self.__students:
                stdscr.addstr(f"{s}\n")

    def list_courses(self, stdscr):
        stdscr.addstr("\n=== DANH SACH MON HOC ===\n\n")
        if not self.__courses:
            stdscr.addstr("Chua co mon hoc nao.\n")
        else:
            for c in self.__courses:
                stdscr.addstr(f"{c}\n")

    def show_marks(self, stdscr):
        stdscr.addstr("\n=== BANG DIEM MON HOC ===\n\n")
        c_id = get_input(stdscr, "Nhap ID mon hoc de xem diem: ")

        if c_id not in self.__marks:
            stdscr.addstr("Chua co bang diem cho mon hoc nay.\n")
        else:
            stdscr.addstr(f"\nBANG DIEM MON {c_id}:\n")
            for s in self.__students:
                s_id = s.get_id()
                score = self.__marks[c_id].get(s_id, "N/A")
                stdscr.addstr(f"ID: {s_id:<8} | Ten: {s.get_name():<20} | Diem: {score}\n")


def get_input(stdscr, prompt):
    """Ham ho tro nhap van ban voi Curses"""
    stdscr.addstr(prompt)
    stdscr.refresh()
    curses.echo()
    input_bytes = stdscr.getstr()
    curses.noecho()
    return input_bytes.decode('utf-8').strip()


def main(stdscr):
    stdscr.scrollok(True)         # Cho phep man hinh tu cuon khi het cho
    curses.curs_set(1)
    app = StudentMarkManagement()

    while True:
        stdscr.addstr("\n===============================================\n")
        stdscr.addstr("  HE THONG QUAN LY DIEM SINH VIEN (PW3 - CURSES)\n")
        stdscr.addstr("===============================================\n")
        stdscr.addstr("1. Nhap thong tin sinh vien\n")
        stdscr.addstr("2. Nhap thong tin mon hoc\n")
        stdscr.addstr("3. Nhap diem cho mon hoc\n")
        stdscr.addstr("4. Hien thi danh sach mon hoc\n")
        stdscr.addstr("5. Hien thi danh sach sinh vien & GPA (Giam dan)\n")
        stdscr.addstr("6. Hien thi bang diem mon hoc\n")
        stdscr.addstr("7. Thoat\n")
        stdscr.addstr("-----------------------------------------------\n")

        choice = get_input(stdscr, "Chon chuc nang (1-7): ")

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