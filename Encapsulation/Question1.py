"""
Docstring for Encapsulation.Question1

Create a ShoppingCart class:

private item list

methods to add/remove items

prevent direct list modification

📌 Focus: preventing direct data access

"""

class ShoppingCart:

    def __init__(self):
     
        self.__items = [] # private
 
    def addItems(self, *items):

        # adding items in the list
        self.__items.extend(items)

    def removeItems(self, *items):

        # removing items from the list
        for item in items:

            if item in self.__items:

                self.__items.remove(item)

    def showItems(self):

        return self.__items.copy()

s = ShoppingCart()
user = input("Enter some value : ")
s.addItems(user)
print(s.showItems())