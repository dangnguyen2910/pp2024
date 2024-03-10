from .department import Department

class Course:
    def __set_ects(self):
        self.__ects = int(input("Enter course's ects: "))
        while self.__ects < 0:
            self.__ects = int(input("Invalid input. Enter course's ects: "))  
        return self.__ects

    def __init__(self, id = None, name = None, ects = None):
        if (id is not None and name is not None and ects is not None):
            self.__id = id
            self.__name = name
            self.__ects = ects
            self.__mark = []
            Department.course_list.append(self)
        else: 
            self.__id = input("Enter course's id: ")
            self.__name = input("Enter course's name: ")
            self.__ects = self.__set_ects()
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

    def to_dict(self):
        return {"id":self.__id, "name":self.__name, "ects":self.__ects}
