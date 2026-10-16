import numpy as np

class StudentMarkManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}  

    # ---------- Them du lieu ----------
    def add_student(self, student):
        self.__students.append(student)

    def add_course(self, course):
        self.__courses.append(course)

    def set_mark(self, course_id, student_id, score):
        if course_id not in self.__marks:
            self.__marks[course_id] = {}
        self.__marks[course_id][student_id] = score

    def reset_marks(self, course_id):
        self.__marks[course_id] = {}

    #  Lay du lieu 
    def get_students(self):
        return self.__students

    def get_courses(self):
        return self.__courses

    def find_course(self, course_id):
        for c in self.__courses:
            if c.get_id() == course_id:
                return c
        return None

    def has_marks(self, course_id):
        return course_id in self.__marks

    def get_mark(self, course_id, student_id, default="N/A"):
        return self.__marks[course_id].get(student_id, default)

    # Tinh toan 
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