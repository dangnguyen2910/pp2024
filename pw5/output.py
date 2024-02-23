import curses 
from domains.department import Department
from domains.student import Student
from domains.course import Course
from domains.mark import Mark


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
        print(user_input)
        location = 0
        if user_input == ord('s') or user_input == ord('S'):
            text_window.clear()
            student_list = open("students.txt","r")
            while True:
                id = student_list.readline().rstrip()
                if not id:
                    break
                name = student_list.readline().rstrip()
                dob = student_list.readline().rstrip()
                gpa = student_list.readline().rstrip()
                text_window.addstr(location ,2 ,f"ID: {id}\tName: {name}\tDOB: {dob}\tGPA: {gpa}")

        elif user_input == ord('c') or user_input == ord('C'):
            text_window.clear()
            course_list = open("courses.txt","r")
            while True:
                id = course_list.readline().rstrip()
                if not id:
                    break
                name = course_list.readline().rstrip()
                ects = course_list.readline().rstrip()
                text_window.addstr(location ,2 ,f"ID: {id}\tName: {name}\tECTS: {ects}")
                location += 1


        elif user_input == ord('m') or user_input == ord('M'):
            text_window.clear()
            mark_list = open("marks.txt","r")
            while True:
                student_id = mark_list.readline().rstrip()
                course_name = mark_list.readline().rstrip()
                mark = mark_list.readline().rstrip()
                if not student_id:
                    break
                text_window.addstr(location ,2 ,f"Student ID: {student_id}\tCourse name: {course_name}\tMark: {mark}")
                location += 1
         

        elif user_input == ord('q') or user_input == ord('Q'):
            return

        text_window.refresh()
