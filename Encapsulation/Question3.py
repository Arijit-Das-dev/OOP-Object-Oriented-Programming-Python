"""
Docstring for Encapsulation.Question3

Design an ATM class:

private PIN

private balance

methods: authenticate, check_balance, withdraw

block operations if PIN is wrong

"""
class ATM:

    def __init__(self, pin, balance):
        self.__pin = pin              # private
        self.__balance = balance      # private
        self.__authenticated = False  # auth state
        self.__attempts = 0

    def authenticate(self, pin):
        if self.__attempts >= 3:
            print("Card blocked")
            return

        if pin == self.__pin:
            self.__authenticated = True
            self.__attempts = 0
            print("Authentication successful")
        else:
            self.__attempts += 1
            print("Wrong PIN")

    def check_balance(self):
        if not self.__authenticated:
            print("Access denied. Authenticate first.")
            return
        return self.__balance

    def withdraw(self, amount):
        if not self.__authenticated:
            print("Access denied. Authenticate first.")
            return

        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")

atm = ATM(1234, 18000)
atm.authenticate(237) # wrong pin