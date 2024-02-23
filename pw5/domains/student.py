from .department import Department
from .mark import Mark

class Student:
    def __init__(self):
        self.__id = input("Enter student's id: ")
        self.__name = input("Enter student's name: ")
        self.__dob = input("Enter student's date of birth: ")
        self.__gpa = 0
        self.__mark = []
        Department.student_list.append(self)

    # def set_department_student_list(self):
    #     dept = Department()
    #     dept.student_list.append()

    def set_mark(self, mark):
        if mark.get_mark() > 0:
            self.__mark.append(mark)
    
    def set_gpa(self, gpa):
        if gpa >= 0 and gpa <= 20:
            self.__gpa = gpa

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def get_gpa(self):
        return self.__gpa

    def get_mark(self):
        return self.__mark

    def show_info(self):
            print(f"ID: {self.__id}\tName: {self.__name}\tDate of birth: {self.__dob}\tGPA: {self.__gpa}")
