"""
Docstring for Inheritance.Multiple-Inheritance.MRO.concept

MRO = Method Resolution Order

order in which Python searches methods
"""

class Parent1:

    def quality1(self):
        print("Parent 1 can sing")

class Parent2:
    
    def quality2(self):
        print("Parent 2 can dance")

class Child(Parent1, Parent2):

    def quality3(self):
        print("Child can perform both")

c = Child()
c.quality1()
c.quality2()
c.quality3()

print(Child.__mro__)

# (<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.Parent2'>, <class 'object'>)