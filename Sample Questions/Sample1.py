""" HOSPITAL MANAGEMENT SYSTEM """


import os

class Person:

    SUBJECT = "Class : Doctor"

    def __init__(self, person_id, name, age, gender, phone, address):

        self.__person_id = person_id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.address = address

        os.makedirs("Details_fld", exist_ok=True)

        with open("Details_fld/Profile.txt", "w") as f:

            details1 = f"""Person id = {self.__person_id}\n, Name = {self.name}\n, Age = {self.age}\n, Gender = {self.gender}\n, Phone = {self.phone}\n, Address = {self.address}"""
            
            f.write(details1)

        print("All Data stored")
        print("="*50)
    
    def update_profile(self, new_folder_name , new_name, new_age, new_gender, new_phone, new_address):
        
        os.makedirs(new_folder_name, exist_ok=True)

        self.name = new_name
        self.age = new_age
        self.gender = new_gender
        self.phone = new_phone
        self.address = new_address

        with open(f"{new_folder_name}/new_profile.txt", "w") as f:

            details2 = f"""name = {self.name}\n age = {self.age}\n new_gender = {self.gender}\n new_phone = {self.phone}\n new_address = {self.address}"""
            f.write(details2)

        print("New data stored")
        print("="*50)
    
    def get_details(self):

        print("Here is your details")
        print("="*50)

        print(f"Your name : {self.name}")
        print(f"Your age : {self.age}")
        print(f"Your Gender : {self.gender}")
        print(f"Your phone : {self.phone}")
        print(f"Your address : {self.address}")

class Doctor(Person):

    SUBJECT = "Class : Doctor"

    def __init__(self, person_id, name, age, gender, phone, address, doctor_id, specialization, experience, fee):
        super().__init__(person_id, name, age, gender, phone, address)

        self.doctor_id = doctor_id
        self.specialization = specialization
        self.experience = experience
        self.fee = fee
        self.medical_history = []

    def add_patient(self):

        super().get_details()
        print("Patient Added")

    def _medical_history(self,  date, doctor, diagnosis, prescription, notes):

        record = {

            "date":date,
            "doctor":doctor,
            "diagnosis": diagnosis,
            "prescription":prescription,
            "notes":notes
        }

        self.medical_history.append(record)

    def show_medical_history(self):

       for record in self.medical_history:
           print(record)

d = Doctor(1, "Arijit", 23, "Male", 6289449233, "Dum Dum", "A1", "Aurthop", 10, 12000)
d.add_patient()
d._medical_history("12-2-2004","A.K Bose", "x", "xyz", "Available")
d.show_medical_history()