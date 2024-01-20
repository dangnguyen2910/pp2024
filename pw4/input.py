from domains.student import Student
from domains.course import Course
from domains.department import Department
from domains.mark import Mark

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
