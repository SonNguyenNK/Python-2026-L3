
students = []  # Lưu tuple: (student_id, name, dob)
courses = []   # Lưu tuple: (course_id, name)
marks = {}     # Lưu dict: {course_id: {student_id: mark}}



def input_students():
    count = int(input("number of students: "))
    for _ in range(count):
        s_id = input("  ID: ")
        name = input("  Ten: ")
        dob = input(" (DoB): ")
        students.append((s_id, name, dob))

def input_courses():
    count = int(input("Number of courses: "))
    for _ in range(count):
        c_id = input("  ID courses: ")
        name = input("  Name courses: ")
        courses.append((c_id, name))

def input_marks():
    list_courses()
    c_id = input("\nNhap ID mon hoc de nhap diem: ")
    marks[c_id] = {}
    print(f"\nNhap diem cho mon ID: {c_id} ")
    for s_id, name, _ in students:
        score = float(input(f"Diem cho sinh vien '{name}' (ID: {s_id}): "))
        marks[c_id][s_id] = score



def list_courses():
    print("\nDANH SACH MON HOC ")
    for c_id, name in courses:
        print(f"ID Mon: {c_id} | Ten Mon: {name}")

def list_students():
    print("\n DANH SACH SINH VIEN ")
    for s_id, name, dob in students:
        print(f"ID: {s_id} | Ten: {name} | Ngay sinh: {dob}")

def show_marks():
    c_id = input("Nhap ID mon hoc de xem diem: ")
    print(f"\nBANG DIEM MON: {c_id}")
    for s_id, name, _ in students:
        score = marks[c_id].get(s_id, "N/A")
        print(f"ID: {s_id} | Ten: {name} | Diem: {score}")



def main():
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
            print("Da thoat chuong trinh.")
            break

if __name__ == "__main__":
    main()

