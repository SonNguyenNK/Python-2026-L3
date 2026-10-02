import math

from domains import Student, Course


def input_students(app):
    print("\nNHAP THONG TIN SINH VIEN")
    count = int(input("Nhap so luong sinh vien: "))

    for i in range(count):
        print(f"\nSinh vien thu {len(app.get_students()) + 1}:")
        s_id = input("ID Sinh vien: ")
        name = input("Ten Sinh vien: ")
        dob = input("DoB: ")
        app.add_student(Student(s_id, name, dob))

    print("-> Da them sinh vien thanh cong!")


def input_courses(app):
    print("\nNHAP THONG TIN MON HOC")
    count = int(input("Nhap so luong mon hoc: "))

    for i in range(count):
        print(f"\nMon hoc thu {len(app.get_courses()) + 1}:")
        c_id = input("ID Mon hoc: ")
        name = input("Ten Mon hoc: ")
        credits = int(input("So tin chi: "))
        app.add_course(Course(c_id, name, credits))

    print("Da them")


def input_marks(app):
    print("\nNHAP DIEM MON HOC")
    if not app.get_courses() or not app.get_students():
        print("Can phai nhap danh sach mon hoc va sinh vien truoc")
        return

    c_id = input("Nhap ID mon hoc de nhap diem: ")
    course = app.find_course(c_id)

    if course is None:
        print("Khong tim thay ID mon hoc nay")
        return

    app.reset_marks(c_id)

    print(f"\nNhap diem cho mon: {course.get_name()}")
    for s in app.get_students():
        raw_score = float(input(f"  Diem cho {s.get_name()} (ID: {s.get_id()}): "))
        # Dung math.floor() lam tron xuong 1 chu so thap phan
        app.set_mark(c_id, s.get_id(), math.floor(raw_score * 10) / 10)

    print("-> Nhap diem xong")


def input_course_id():
    print("\nBANG DIEM MON HOC ")
    return input("Nhap ID mon hoc de xem diem: ")