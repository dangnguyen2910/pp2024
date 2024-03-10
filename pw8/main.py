from domains import *
from input import *
import curses
from output import design_ui 
import zlib
import threading

class DecompressThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        decompression()

class CompressThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        try:
            compression()
        except Exception:
            pass

# Start decompress in background
decompress_thread = DecompressThread()
decompress_thread.start()

choice = input("Do you want to add any new data? (y/n)")
if (choice == "y"):
    init_students()
    init_courses()
    input_marks()

    Department.calculate_gpa()
    Department.sort_student_list()

# Start compress in background
compress_thread = CompressThread()
compress_thread.start()

curses.wrapper(design_ui)
