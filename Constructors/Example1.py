"""
Docstring for Constructors.Example1
"""
# __init__(self) function
# All classes have a function called __init__(), which is always excecuted when the class is being initiated.
# self is a keyword which refers to the current object that is being created
# That __init__() function can call itself when we create new object of the class

class Student:

    def __init__(self):

        print("Example1")
        print("Example2")
        print(self)

s1 = Student()