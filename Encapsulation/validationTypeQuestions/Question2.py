"""
Docstring for Encapsulation.validationTypeQuestions.Question2

Create a class where username cannot be changed once set.
"""

class Username:

    def __init__(self, username):
        
        self.__username = username

    def show(self):

        return self.__username
    
u = Username("alex@123")
print(u.show())