from .department import Department
from .mark import Mark

class Student:
    def __init__(self, id = None, name = None, dob = None, gpa = None):
        if (id is not None and name is not None and dob  is not None and gpa  is not None):
            self.__id = id
            self.__name = name
            self.__dob = dob
            self.__gpa = gpa
            self.__mark = []
            Department.student_list.append(self)

        else:
            self.__id = input("Enter student's id: ")
            self.__name = input("Enter student's name: ")
            self.__dob = input("Enter student's date of birth: ")
            self.__gpa = 0
            self.__mark = []
            Department.student_list.append(self)


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

    def to_dict(self):
        mark_list = []

        for mark in self.__mark:
            mark_list.append(mark.to_dict())

        return {"id":self.__id, "name":self.__name, "dob":self.__dob, "gpa":self.__gpa, "mark":mark_list }
