"""
Docstring for Keywords.delete

used to delete object properties or object itself
"""


class Student:

    def __init__(self, name, sec, dept, location):

        self.name = name
        self.sec = sec
        self.dept = dept
        self.location = location

s1 = Student("Alex", "B", "B.TECH", "Kolkata")
print(s1.name, s1.sec, s1.dept, s1.location)