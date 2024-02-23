from domains.student import Student
from domains.course import Course
from domains.department import Department
from domains.mark import Mark
import zipfile
import os
import pathlib

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


def write_to_student_file():
    with open("students.txt","a") as student_file:
        for student in Department.student_list:
            student_file.write(f"{student.get_id()}\n{student.get_name()}\n{student.get_dob()}\n{round(student.get_gpa(),2)}")

def write_to_course_file():
    with open("courses.txt","a") as course_file:
        for course in Department.course_list:
            course_file.write(f"{course.get_id()}\n{course.get_name()}\n{course.get_ects()}")

def write_to_mark_file():
    with open("marks.txt", "a") as mark_file:
        for mark in Department.mark_list:
            mark_file.write(f"{mark.get_student_id()}\n{mark.get_course_name()}\n{mark.get_mark()}")


def compression():
    compression = zipfile.ZIP_DEFLATED
    compressed_file = zipfile.ZipFile("students.dat",mode = "w")
    try:
        txt_files = ["students.txt","courses.txt","marks.txt"]
        for file in txt_files:
            compressed_file.write(file,compress_type = compression)
            os.remove(file)
    except Exception as e:
        print (e)
    finally: 
        compressed_file.close()

def decompression():
    try: 
        file = zipfile.ZipFile("students.dat","r")
        file.extractall()
        os.remove("students.dat")
    except Exception:
        pass
