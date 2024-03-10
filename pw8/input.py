from domains.student import Student
from domains.course import Course
from domains.department import Department
from domains.mark import Mark
import pickle
import os

def init_students():
    num_of_students = int(input("Enter number of students: "))
    for _ in range (num_of_students):
        student = Student()

def init_courses():
    num_of_courses = int(input("Enter number of courses: "))
    for _ in range (num_of_courses):
        course = Course()

def input_marks():
    for student in Department.student_list:
        for course in Department.course_list:
            mark = Mark(student.get_id(), course.get_name(), course.get_ects())


def compression():
    with open("students.dat","wb") as f:
        student_list = []
        for student in Department.student_list:
            student_list.append(student.to_dict())  
        pickle.dump(student_list,f)
    with open("courses.dat","wb") as f:
        course_list = []
        for course in Department.course_list:
            course_list.append(course.to_dict())
        pickle.dump(course_list, f)

    with open("marks.dat", "wb") as f:
        mark_list = []
        for mark in Department.mark_list:
            mark_list.append(mark.to_dict())
        pickle.dump(mark_list,f)


def decompression():
    try: 
        with open("students.dat","rb") as f:
            student_list = pickle.load(f)
            for student in student_list:
                student = Student(id = student['id'],name = student['name'], dob = student['dob'], gpa = student['gpa'])
        os.remove("students.dat")
    except Exception:
        pass
    try:
        with open("courses.dat","rb") as f:
            course_list = pickle.load(f)
            for course in course_list:
                course = Course(id = course['id'],name = course['name'], ects = course['ects'])
        os.remove("courses.dat")
    except Exception:
        pass
    
    try:
        with open("marks.dat", "rb") as f:
            mark_list = pickle.load(f)
            for mark in mark_list:
                mark = Mark(mark['student_id'], mark['course_name'], mark['course_ects'], mark = mark['mark'])
        os.remove("marks.dat")
    except Exception:
        pass

