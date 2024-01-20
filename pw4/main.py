from domains import *
from input import *
import curses
from output import design_ui 

init_students()
init_courses()
input_marks()
Department.calculate_gpa()
Department.sort_student_list()

curses.wrapper(design_ui)
