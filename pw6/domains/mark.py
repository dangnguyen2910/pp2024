import math
from .department import Department

class Mark:
    def __init__(self, student_id, course_name, course_ects, mark=None):
        self.__student_id = student_id
        self.__course_name = course_name
        self.__course_ects = course_ects
        if (mark is None):
            self.__mark = math.floor(float(input(f"Course: {self.__course_name}. Student ID: {self.__student_id}. Marks: ")))
        else:
            self.__mark = mark
        
        Department.mark_list.append(self)

        for student in Department.student_list:
            if student.get_id() == self.__student_id:
                student.set_mark(self)

        for course in Department.course_list:
            if course.get_name() == self.__course_name:
                course.set_mark(self)

    def get_ects(self):
        return self.__course_ects

    def get_student_id(self):
        return self.__student_id

    def get_course_name(self):
        return self.__course_name

    def get_mark(self):
        return self.__mark

    def to_dict(self):
        return {"student_id":self.__student_id, "course_name": self.__course_name, "course_ects": self.__course_ects, "mark":self.__mark}
