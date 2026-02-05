"""
Docstring for Inheritance.Keyword.SingleInheritance
"""

class Person:

    def __init__(self, name, age):
        
        self.name = name
        self.age = age

class Student(Person):

    def __init__(self, name, age, roll):
        super().__init__(name, age)

        self.roll = roll

s = Student("Alex", "45", 56)
# accessing person class property via student class
print(s.name, s.age)