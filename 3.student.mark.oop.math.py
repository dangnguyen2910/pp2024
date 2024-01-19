import math
import numpy as np 
import curses 

class Student:
    def __init__(self):
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



class Course:
    def __set_ects(self):
        self.__ects = int(input("Enter course's ects: "))
        while self.__ects < 0:
            self.__ects = int(input("Invalid input. Enter course's ects: "))  
        return self.__ects

    def __init__(self):
        self.__id = input("Enter course's id: ")
        self.__name = input("Enter course's name: ")
        self.__ects = self.__set_ects()
        self.__student_list = Department.student_list
        self.__mark = []
        Department.course_list.append(self)


    def set_mark(self, mark):
        if mark.get_mark() > 0:
            self.__mark.append(mark)

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_ects(self):
        return self.__ects

    def show_info(self):
        print(f"ID: {self.__id}\tName: {self.__name}\tECTS: {self.__ects}")



class Mark:
    def __init__(self, student_id, course_name, course_ects):
        self.__student_id = student_id
        self.__course_name = course_name
        self.__course_ects = course_ects
        self.__mark = math.floor(float(input(f"Course: {self.__course_name}. Student ID: {self.__student_id}. Marks: ")))
        
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


class Department:
    student_list = []
    course_list = []
    mark_list = []

    @staticmethod
    def calculate_gpa():
        for student in Department.student_list:
            mark_list = np.array([mark.get_mark() for mark in student.get_mark()])
            ects_list = np.array([mark.get_ects() for mark in student.get_mark()])
            student.set_gpa(np.dot(mark_list,ects_list)/ np.sum(ects_list)) 

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


def design_ui(stdscr):
    stdscr.clear()
    curses.curs_set(False)

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)

    # stdscr.addstr(curses.LINES-1, 0, "Q: Quit")
    stdscr.addstr(curses.LINES-1, 0, "S: Student list   C: Course list   M: Mark list   Q:Quit")

    # Change q's color 
    stdscr.chgat(curses.LINES-1, 50, 1, curses.A_BOLD | curses.color_pair(1))

    # Change s, c, m color
    stdscr.chgat(curses.LINES-1, 0, 1, curses.A_BOLD | curses.color_pair(2))
    stdscr.chgat(curses.LINES-1, 18, 1, curses.A_BOLD | curses.color_pair(2))
    stdscr.chgat(curses.LINES-1, 35, 1, curses.A_BOLD | curses.color_pair(2))

    # Add title
    stdscr.addstr(0, 3, "STUDENT MANAGEMENT APPLICATION", curses.A_BOLD)

    # Create a box inside terminal
    representation_window = curses.newwin(curses.LINES-2, curses.COLS-2, 1,1)
    representation_window.box()

    stdscr.refresh()
    representation_window.refresh()

    text_window = representation_window.subwin(curses.LINES-4, curses.COLS-4, 2,2)

    # Print information to screen
    while True:
        user_input = representation_window.getch()
        location = 0
        if user_input == ord('s') or user_input == ord('S'):
            text_window.clear()
            for student in Department.student_list:
                text_window.addstr(location ,2 ,f"ID: {student.get_id()}\tName: {student.get_name()}\tDOB: {student.get_dob()}\tGPA: {round(student.get_gpa(),2)}")
                location += 1

        elif user_input == ord('c') or user_input == ord('C'):
            text_window.clear()
            for course in Department.course_list:
                text_window.addstr(location ,2 ,f"ID: {course.get_id()}\tName: {course.get_name()}\tECTS: {course.get_ects()}")
                location += 1

        elif user_input == ord('m') or user_input == ord('M'):
            text_window.clear()
            for mark in Department.mark_list:
                text_window.addstr(location ,2 ,f"Student ID: {mark.get_student_id()}\tCourse name: {mark.get_course_name()}\tMark: {mark.get_mark()}")
                location += 1
         
        elif user_input == ord('q') or user_input == ord('Q'):
            return

        text_window.refresh()



    
init_students()
init_courses()
input_marks()
Department.calculate_gpa()
Department.sort_student_list()

curses.wrapper(design_ui)
# Department.show_all()
