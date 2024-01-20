import numpy as np

class Department:
    student_list = []
    course_list = []
    mark_list = []

    @staticmethod
    def calculate_gpa():
        for student in Department.student_list:
            student_mark_list = np.array([mark.get_mark() for mark in student.get_mark()])
            course_ects_list = np.array([mark.get_ects() for mark in student.get_mark()])
            student.set_gpa(np.dot(student_mark_list,course_ects_list)/ np.sum(course_ects_list)) 

    @staticmethod
    def sort_student_list():
        Department.student_list = sorted(Department.student_list, key=lambda student : student.get_gpa(), reverse=True)

    @staticmethod
    def show_all(show_student = True, show_course = True):
        if show_student:
            for student in Department.student_list:
                print(f"ID: {student.get_id()}\tName: {student.get_name()}\tDOB: {student.get_dob()}\tGPA: {student.get_gpa()}")

        if show_course:
            for course in Department.course_list:
                print(f"ID: {course.get_id()}\t\
                        Name: {course.get_name()}\t\
                        ECTS: {course.get_ects()}")
