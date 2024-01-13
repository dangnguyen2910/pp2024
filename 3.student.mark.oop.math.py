import math
import numpy as np 

class Student:
    def __init__(self):
        self.__id = input("Enter student's id: ")
        self.__name = input("Enter student's name: ")
        self.__dob = input("Enter student's date of birth: ")
        self.__gpa = 0
        # student_list.append(self)
    
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def cal_gpa(self, course_list):
        ects = mark = np.array([])
        for course in course_list:
            ects = np.append(ects,course.get_ects())
            for id_mark_dict in course.get_mark_list():
                id_list = list(id_mark_dict.keys())
                id = id_list[0]
                if self.__id == id:
                    mark = np.append(mark, id_mark_dict[id])
                    break
        self.__gpa = np.dot(mark,ects)/ np.sum(ects)


    def show_info(self):
            print(f"ID: {self.__id}\tName: {self.__name}\tDate of birth: {self.__dob}\tGPA: {self.__gpa}")
    
    @staticmethod
    def show_all(student_list):
        for student in student_list:
            # print(f"ID: {student.__id}\tName: {student.__name}\tDate of birth: {student.__dob}GPA: {student.__gpa}")            
            student.show_info()    

# class Class:
#     def __init__(self, student_list):
#         self.__name = input("Enter class name: ")
#         self.__student_list = student_list

#     def get_name(self):
#         return self. __name

#     def get_student_list(self):
#         return self.__student_list;


class Course:
    def __init__(self, student_list):
        self.__id = input("Enter course's id: ")
        self.__name = input("Enter course's name: ")
        self.__ects = int(input("Enter course's ects: "))
        while self.__ects < 0:
            self.__ects = int(input("Invalid input. Enter course's ects: "))  

        self.__student_list = student_list
        # self.__classes = class_list
        self.__mark = []

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_ects(self):
        return self.__ects

    # def get_class_list(self):
    #     return self.__classes

    def get_mark_list(self):
        return self.__mark

    def input_marks(self):
        print(f"Input marks for course {self.__name}")
        for student in self.__student_list:
            id = student.get_id()
            mark = math.floor(float(input(f"Enter mark for student {student.get_id()}: ")))
            self.__mark.append({id : mark})
                

    def show_info(self):
        print(f"ID: {self.__id}\tName: {self.__name}\tECTS: {self.__ects}")

        for student in self.__mark:
            id_list = list(student.keys())
            id = id_list[0]
            score = student[id]
            print (f"\tID: {id}\tScore: {score}")

    @staticmethod
    def show_all(course_list):
        for course in course_list:
            course.show_info()


student_list = []
num_of_students = int(input("Enter number of students: "))
for _ in range (num_of_students):
    student = Student()
    student_list.append(student);

# class_list = []
# class1 = Class(student_list)
# class_list.append(class1)

course_list = []
num_of_courses = int(input("Enter number of courses: "))
for _ in range (num_of_courses):
    course = Course(student_list)
    course_list.append(course)
    course.input_marks()


for student in student_list:
    student.cal_gpa(course_list)


Course.show_all(course_list)
Student.show_all(student_list)

