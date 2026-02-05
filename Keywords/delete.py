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
del s1.name
del s1.sec
print(s1.name, s1.sec, s1.dept, s1.location) # Here name and sec property does not exist any more and it will throw an error