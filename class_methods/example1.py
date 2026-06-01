"""
We can not directly change the values of class attributes,
thats why we need @classmethods
"""

class Student:

    name = "ABC"

    def changeName(self, newName):

        self.name = newName

s = Student()
s.changeName("XYZ")
print(Student.name) # the value of class attribute "ABC" remains the same