"""
Docstring for Inheritance.Multi-Level-Inheritance.Question1

structure:
[Grandparent => Parent => Child]

Syntax:
{
class GrandParent:

    def method1(self):
        pass
    
class Parent(GrandParent):

    def method2(self):
        pass
        
class Child(Parent):

    def method3(self):
        pass
}   
"""

""" QUESTION 1 =>

Design classes:

Person → Employee → Manager

Person stores name

Employee stores employee ID

Manager stores team size
Write code to access all details using a Manager object.

"""

class Person:

    subject = "Company details management system"

    def __init__(self, name):
        
        self.name = name

class Employee(Person):

    def __init__(self, name, emp_id):
        super().__init__(name)

        self.emp_id = emp_id

class Manager(Employee):

    def __init__(self, name, emp_id, team_size):
        super().__init__(name, emp_id)

        self.team_size = team_size

m = Manager("Arijit", "2245", 5)
print(m.subject)
print(m.emp_id)
print(m.name)
print(m.team_size)