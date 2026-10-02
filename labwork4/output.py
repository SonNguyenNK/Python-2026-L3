def show_menu():
    print("  HE THONG QUAN LY DIEM SINH VIEN (PW4)")
    print("1. Nhap thong tin sinh vien")
    print("2. Nhap thong tin mon hoc")
    print("3. Nhap diem cho mon hoc")
    print("4. Hien thi danh sach mon hoc")
    print("5. Hien thi danh sach sinh vien & GPA (Giam dan)")
    print("6. Hien thi bang diem mon hoc")
    print("7. Thoat")


def list_courses(app):
    print("\nDANH SACH MON HOC")
    if not app.get_courses():
        print("Chua co mon hoc nao.")
    else:
        for c in app.get_courses():
            print(c)


def list_students(app):
    print("\nDANH SACH SINH VIEN")
    if not app.get_students():
        print("Chua co sinh vien nao.")
    else:
        app.sort_students_by_gpa()
        for s in app.get_students():
            print(s)


def show_marks(app, c_id):
    if not app.has_marks(c_id):
        print("Chua co bang diem cho mon hoc nay.")
    else:
        print(f"\nBANG DIEM MON {c_id}:")
        for s in app.get_students():
            score = app.get_mark(c_id, s.get_id())
            print(f"ID: {s.get_id():<8} | Ten: {s.get_name():<20} | Diem: {score}")