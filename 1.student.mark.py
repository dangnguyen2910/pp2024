#input student information
def set_student():
    student = {}
    student['name'] = input("Enter student's name: ")
    student['id'] = input("Enter student's id: ")
    student['dob'] = input("Enter student's date of birth: ")
    return student

#input course's information: id, name, classes in this course
def set_course(class_list):
    course = {}
    course['id'] = input("Enter course's id: ")
    course['name'] = input("Enter course's name: ")
    course['classes'] = class_list
    return course

#input marks of students in this course
def input_marks(course, class_list):
    course['marks'] = []
    for student_class in class_list:
        for student in student_class:
            score = input(f'Enter score for student with id {student["id"]} in course {course["name"]}: ')
            course['marks'].append({student["id"] : score}) 


def show_courses(course_list):
    print('List of courses: ')
    for course in course_list:
        print(f'  -  {course["name"]}')


def show_students(class_list):
    print('Student list: ')
    for student_class in class_list:
        for student in student_class:
            print(f'ID: {student["id"]}\tName: {student["name"]}\tDate of birth: {student["dob"]}')


def show_student_marks(course):
    print(f"Students' scores in course {course['name']}")
    for student_marks in course['marks']:
        key_list = list(student_marks.keys())
        id = key_list[0]
        score = student_marks[id]
        print (f"ID: {id}\tScore: {score}")

#----------------------------------------------------------------------------------------
student1 = set_student()

ict = []
ds = []
cs = []

class_list = []
class_list += [ict, ds, cs]

ict+=[student1]

course_list = []
advanced_python = set_course(class_list)
course_list += [advanced_python]
input_marks(advanced_python, class_list)


show_courses(course_list)
show_students(class_list)
show_student_marks(course_list[0])

