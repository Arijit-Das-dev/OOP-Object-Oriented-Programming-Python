class Student:
    name = "ABC"

    @classmethod
    def changeName(self, newName):
        self.name = newName

s = Student()
s.changeName("XYZ")
print(Student.name) # By using @classmethod, we can directly change the class attribute