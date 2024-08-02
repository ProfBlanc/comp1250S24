"""
Colleges have programs
Program have Courses
Course's have Grades

"""
class Grade:
    def __init__(self, mark):
        self.mark = mark

    @property
    def mark(self):
        return self.__mark
    @mark.setter
    def mark(self, value):
        self.__mark = 0
        self.__mark = value if value >= 0 and value<=100 else 0


class Course:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value if isinstance(value, str) and \
        len(value) >= 3 else "Course Name"

    @property
    def grade(self):
        return self.__grade
    @grade.setter
    def grade(self, value):
        if isinstance(value, int):
            self.__grade = Grade(value)


