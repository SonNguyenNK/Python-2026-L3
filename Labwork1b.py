class Student:
    """Lop dai dien cho Sinh vien"""
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
        self.__id = input("  ID: ")
        self.__name = input("  Ten: ")
        self.__dob = input("  (DoB): ")

    def __str__(self):
        return f"ID: {self.__id} | Ten: {self.__name} | Ngay sinh: {self.__dob}"


class Course:
    """Lop dai dien cho Mon hoc"""
    def __init__(self, course_id="", name=""):
        self.__id = course_id
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def input_info(self):
        self.__id = input("  ID courses: ")
        self.__name = input("  Name courses: ")

    def __str__(self):
        return f"ID Mon: {self.__id} | Ten Mon: {self.__name}"


class StudentMarkManagement:
    """Lop quan ly he thong"""
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}  # {course_id: {student_id: mark}}

    def input_students(self):
        count = int(input("number of students: "))
        for _ in range(count):
            s = Student()
            s.input_info()
            self.__students.append(s)

    def input_courses(self):
        count = int(input("Number of courses: "))
        for _ in range(count):
            c = Course()
            c.input_info()
            self.__courses.append(c)

    def input_marks(self):
        self.list_courses()
        c_id = input("\nNhap ID mon hoc de nhap diem: ")
        self.__marks[c_id] = {}
        print(f"\nNhap diem cho mon ID: {c_id} ")
        for s in self.__students:
            score = float(input(f"Diem cho sinh vien '{s.get_name()}' (ID: {s.get_id()}): "))
            self.__marks[c_id][s.get_id()] = score

    def list_courses(self):
        print("\nDANH SACH MON HOC ")
        for c in self.__courses:
            print(c)

    def list_students(self):
        print("\n DANH SACH SINH VIEN ")
        for s in self.__students:
            print(s)

    def show_marks(self):
        c_id = input("Nhap ID mon hoc de xem diem: ")
        print(f"\nBANG DIEM MON: {c_id}")
        for s in self.__students:
            score = self.__marks[c_id].get(s.get_id(), "N/A")
            print(f"ID: {s.get_id()} | Ten: {s.get_name()} | Diem: {score}")


def main():
    app = StudentMarkManagement()

    while True:
        print("\nMENU QUAN LY ")
        print("1. Nhap thong tin sinh vien")
        print("2. Nhap thong tin mon hoc")
        print("3. Nhap diem cho mon hoc")
        print("4. Hien thi danh sach mon hoc")
        print("5. Hien thi danh sach sinh vien")
        print("6. Hien thi bang diem mon hoc")
        print("7. Thoat")

        choice = input("Chon chuc nang (1-7): ")

        if choice == '1':
            app.input_students()
        elif choice == '2':
            app.input_courses()
        elif choice == '3':
            app.input_marks()
        elif choice == '4':
            app.list_courses()
        elif choice == '5':
            app.list_students()
        elif choice == '6':
            app.show_marks()
        elif choice == '7':
            print("Da thoat chuong trinh.")
            break


if __name__ == "__main__":
    main()