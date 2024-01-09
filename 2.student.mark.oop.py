class Student:
    def __init__(self, student_list):
        self.__id = input("Enter student's id: ")
        self.__name = input("Enter student's name: ")
        self.__dob = input("Enter student's date of birth: ")
        student_list.append(self)
    
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def show_info(self):
            print(f"ID: {self.__id}\tName: {self.__name}\tDate of birth: {self.__dob}")
    
    @staticmethod
    def show_all(student_list):
        for student in student_list:
            print(f"ID: {student.__id}\tName: {student.__name}\tDate of birth: {student.__dob}")            
    

class Class:
    def __init__(self, student_list, class_list):
        self.__name = input("Enter class name: ")
        self.__student_list = student_list
        class_list.append(self)

    def get_name(self):
        return self. __name

    def get_student_list(self):
        return self.__student_list;


class Course:
    def __init__(self, class_list, course_list):
        self.__id = input("Enter course's id: ")
        self.__name = input("Enter course's name: ")
        self.__classes = class_list
        self.__mark = []
        course_list.append(self)

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_class_list(self):
        return self.__classes

    def input_marks(self):
        print(f"Input marks for course {self.__name}")
        for group in self.__classes:
            for student in group.get_student_list():
                id = student.get_id()
                mark = input(f"Enter mark for student {student.get_id()}: ")
                self.__mark.append({id : mark})
                

    def show_info(self):
        classes = [group.get_name() for group in self.__classes]
        print(f"ID: {self.__id}\tName: {self.__name}\tClass list: {classes}")

        for student in self.__mark:
            key_list = list(student.keys())
            id = key_list[0]
            score = student[id]
            print (f"\tID: {id}\tScore: {score}")


student_list = []
num_of_students = int(input("Enter number of students: "))
for _ in range (num_of_students):
    student = Student(student_list)

class_list = []
class1 = Class(student_list, class_list)

course_list = []
course1 = Course(class_list, course_list)

# student_list[0].show_info()
Student.show_all(student_list)
course1.input_marks()
course1.show_info()
