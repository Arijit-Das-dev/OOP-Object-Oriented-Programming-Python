"""
Docstring for Encapsulation.Example2 => Private
"""
# Private method
class BankAccount1:

    def __init__(self, acc_name, acc_num, password, balance):
        
        self.acc_name = acc_name 
        self.__acc_num = acc_num # private - This is not accessible 
        self.__password = password # private
        self.balance = balance

B = BankAccount1("Arijit", 1234, "a2#@123", 90000)
print(B.acc_name)
print(B.__acc_num) # From this line compiler will throw an error
print(B.__password) 
print(B.balance)

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