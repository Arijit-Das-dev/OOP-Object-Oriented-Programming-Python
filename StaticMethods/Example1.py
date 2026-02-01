"""
Docstring for StaticMethods.Example1

Methods that won't use self param (work at class level)

-> when a method in a class doesn't connect to other methods of that class then we set it as @statismethod
"""

class College:

    def __init__(self, name, sec, dept):
        
        self.name = name
        self.sec = sec
        self.dept = dept

    def showDetails(self): # Class Method

        print(f" Full name : ",self.name)
        print(f" Student section : ",self.sec)
        print(f" Student Department : ",self.dept)

    @staticmethod 
    def college(): # that function dont need any self parameter thats why we use static method
        print("Static method example")
    
c = College("Alex", "A", "BCA")
c.college()