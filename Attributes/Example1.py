"""
Docstring for Attributes.Example1
"""

"""
Attributes are two types =>

1. class attributes
2. Object attributes

=> class.attr
=> obj.attr

**Note : 

All the objects attributes will be different
All the class attributes will be same
"""
class College:

    college_name = "XYZ" # Class attribute

    def __init__(self, name, sec, dept):
        
        # Object attribute
        self.name = name
        self.sec = sec
        self.dept = dept

s1 = College("Alex", "B", "B.Tech")
print(s1.college_name)
print(s1.dept, s1.sec, s1.dept)

s2 = College("Adam", "A", "BBA")
print(s2.college_name)
print(s2.name, s2.sec, s2.dept)