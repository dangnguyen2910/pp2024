from domains import *
from input import *
import curses
from output import design_ui 
import zlib

decompression()

choice = input("Do you want to add any new data? (y/n)")
if (choice == "y"):
    init_students()
    init_courses()
    input_marks()

    Department.calculate_gpa()
    Department.sort_student_list()

curses.wrapper(design_ui)

try: 
    compression()
except FileNotFoundError:
    pass

