"""
Docstring for Inheritance.Multi-Level-Inheritance.Queston2
"""

"""
Authentication Flow

User → AuthenticatedUser → AdminUser

Parent validates username

Middle class validates password

Child validates admin privileges

"""

class User:

    subject = "Authentication Flow"

    def __init__(self, username):
        
        self.username = username

class AuthenticatedUser(User):

    def __init__(self, username, password):
        super().__init__(username)

        self.password = password

class AdminUser(AuthenticatedUser):

    def __init__(self, username, password):
        super().__init__(username, password)

        self.empty_name_memory = []
        self.empty_pass_memory = []
    
    def savedMemory(self):

        self.empty_name_memory.append(self.username)
        self.empty_pass_memory.append(self.password)

    def showDetails(self):

        copied_name = self.empty_name_memory.copy()
        copied_pass = self.empty_pass_memory.copy()

        for name in copied_name:

            print(f"USERNAME : {name}")
        
        for passw in copied_pass:

            print(f"PASSWORD : {passw}")

adm_user = AdminUser("adam", "adam@123#45%45$3")
print(adm_user.subject)
adm_user.savedMemory()
adm_user.showDetails()