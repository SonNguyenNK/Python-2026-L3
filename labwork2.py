class Student:
    def __init__(self, student_id="", name="", dob=""):
        self.__id =student_id
        self.__name = name
        self.__dob = dob

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_dob(self):
        return self.__dob

        def input_info(self):
                self.__id = input("id: ")
                self.__name = input("name: ")
                self.__dob = input("dob: ")


    def display(self):
        print(f"id: {self.__id}| name: {self.__name} | dob: {self.__dob}")
    def __str__(self):
        return f"id: {self.__id}| name: {self.__name} | dob: {self.__dob}"


class Course:
    def __init__(self, course_id="", name=""):
        self.__id = course_id
        self.__name = name

    # Getter methods
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    # Phương thức nhập thông tin môn học
    def input_info(self):
        self.__id = input("  ID courses: ")
        self.__name = input("  Name courses: ")

    def display(self):
        print(f"ID Mon: {self.__id} | Ten Mon: {self.__name}")

    def __str__(self):
        return f"ID Mon: {self.__id} | Ten Mon: {self.__name}"


class StudentMarkManagement:
    """Lớp quản lý danh sách sinh viên, môn học và bảng điểm"""
    def __init__(self):
        self.__students = []  # Chứa danh sách các đối tượng Student
        self.__courses = []   # Chứa danh sách các đối tượng Course
        self.__marks = {}     

    def input_students(self):
        count = int(input("Number of students: "))
        for _ in range(count):
            print(f"\nNhap sinh vien thu {len(self.__students) + 1}:")
            s = Student()
            s.input_info()
            self.__students.append(s)

    def input_courses(self):
        count = int(input("Number of courses: "))
        for _ in range(count):
            print(f"\nNhap mon hoc thu {len(self.__courses) + 1}:")
            c = Course()
            c.input_info()
            self.__courses.append(c)

    def list_courses(self):
        print("\nDANH SACH MON HOC")
        if not self.__courses:
            print("Chua co mon hoc nao.")
            return
        for c in self.__courses:
            c.display()

    def list_students(self):
        print("\nDANH SACH SINH VIEN")
        if not self.__students:
            print("Chua co sinh vien nao.")
            return
        for s in self.__students:
            s.display()

    def input_marks(self):
        if not self.__courses:
            print("Chua co mon hoc nao! Vui long nhap mon hoc truoc.")
            return
        if not self.__students:
            print("Chua co sinh vien nao! Vui long nhap sinh vien truoc.")
            return

        self.list_courses()
        c_id = input("\nNhap ID mon hoc de nhap diem: ")

        # Kiểm tra môn học có tồn tại hay không
        course_exists = any(c.get_id() == c_id for c in self.__courses)
        if not course_exists:
            print("ID mon hoc khong hop le!")
            return

        if c_id not in self.__marks:
            self.__marks[c_id] = {}

        print(f"\nNhap diem cho mon ID: {c_id}")
        for s in self.__students:
            score = float(input(f"Diem cho sinh vien '{s.get_name()}' (ID: {s.get_id()}): "))
            self.__marks[c_id][s.get_id()] = score

    def show_marks(self):
        if not self.__marks:
            print("Chua co bang diem nao duoc nhap.")
            return

        c_id = input("Nhap ID mon hoc de xem diem: ")
        if c_id not in self.__marks:
            print(f"Chua co diem cho mon hoc ID: {c_id}")
            return

        print(f"\n--- BANG DIEM MON: {c_id} ---")
        for s in self.__students:
            s_id = s.get_id()
            score = self.__marks[c_id].get(s_id, "N/A")
            print(f"ID: {s_id} | Ten: {s.get_name()} | Diem: {score}")

    def main_menu(self):
        while True:
            print("\n=== MENU QUAN LY (OOP) ===")
            print("1. Nhap thong tin sinh vien")
            print("2. Nhap thong tin mon hoc")
            print("3. Nhap diem cho mon hoc")
            print("4. Hien thi danh sach mon hoc")
            print("5. Hien thi danh sach sinh vien")
            print("6. Hien thi bang diem mon hoc")
            print("7. Thoat")

            choice = input("Chon chuc nang (1-7): ")

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
                print("Da thoat chuong trinh.")
                break
            else:
                print("Luy chon khong hop le. Vui long chon lai!")


if __name__ == "__main__":
    app = StudentMarkManagement()
    app.main_menu()

    

