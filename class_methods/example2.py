class Student:
    name = "ABC"

    def changeName(self, newName):
        self.__class__.name = newName

s = Student()
s.changeName("XYZ")
print(Student.name) # now that is changed by using __class__