
class User:

    def __init__(self, name, email, password, confirm_password, dob):
        
        self.name = name
        self._email = email
        self.__password = password
        self.__confirm_password = confirm_password
        self.dob = dob

    def save_details(self):

        with open("details.txt", "a") as f:
        
            list_of_details = f"{self.name}, {self.dob}, {self._email}, {self.__confirm_password}"

            f.write(list_of_details)

        return "Details saved successfully"
