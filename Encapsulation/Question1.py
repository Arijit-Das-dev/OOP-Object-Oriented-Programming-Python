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
        self.__items.remove(items)
    
    def showItems(self):

        return self.__items
    
s = ShoppingCart()
s.addItems("a", "b" )
print(s.showItems())