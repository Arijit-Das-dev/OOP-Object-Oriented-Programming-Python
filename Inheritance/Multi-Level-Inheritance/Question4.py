
class User:

    def __init__(self, name, email, password, confirm_password, dob):
        
        self.name = name
        self._email = email
        self.__password = password
        self.__confirm_password = confirm_password
        self.dob = dob

    def save_details(self):

        with open("details.txt", "a") as f:
        
            list_of_details = f"{self.name}, \n{self.dob}, \n{self._email}, \n{self.__confirm_password}\n\n\n"

            f.write(list_of_details)

        return "Details saved successfully"

u = User("Alex", "alex123@gmail.com", "alex@12#23", "alex@12#23", "2004-12-6")
print(u.save_details())