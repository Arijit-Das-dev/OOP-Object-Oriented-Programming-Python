"""
Docstring for Encapsulation.Example2
"""

class BankAccount1:

    def __init__(self, acc_name, acc_num, password, balance):
        
        self.acc_name = acc_name 
        self.__acc_num = acc_num # private - This is not accessible 
        self.__password = password # private
        self.balance = balance
    


# We can access any private attribute value by creating a method
class BankAccount2:

    def __init__(self, acc_name, acc_num, password, balance):
        
        self.acc_name = acc_name 
        self.__acc_num = acc_num # private - This is not accessible 
        self.__password = password # private
        self.balance = balance
    
    def showDetails(self):

        print("Account name : ",self.acc_name)
        print("Account password : ",self.__password)
        print("Account number : ",self.__acc_num)

B = BankAccount2("Arijit", 1234, "a2#@123", 90000)
B.showDetails()