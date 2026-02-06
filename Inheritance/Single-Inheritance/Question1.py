"""
Docstring for Inheritance.SingleInheritance

def => reusing one class inside another class

Example :

One class have it's own quality or method same as another class wants the same or extra quality with the previous
Structure: 

One Parent -> One child

**Note: By inheritance we can access another class methods + properties
        we can access public and protected properties except private property
"""

# Syntax
"""
class Parent:

    pass

class Child(Parent):

    pass
    
"""
# Example 1
class Person:

    def speak(self):

        print("I can speak")

class Student(Person):
    pass

s = Student()
s.speak()


# Example 2
class Person1:

    name = "XYZ"

class Person2(Person1):

    pass

p = Person2()
print(p.name)