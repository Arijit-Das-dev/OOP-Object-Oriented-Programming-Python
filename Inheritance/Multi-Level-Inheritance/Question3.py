"""
Docstring for Inheritance.Multi-Level-Inheritance.Question3
"""
"""
Hospital System

Person → Patient → InPatient

Patient has disease info

InPatient has room number & admission date

"""

class Person:

    subject = "Hospital system"

    def __init__(self, p_id, p_name, p_loc, p_adhaar):
        
        self.p_id = p_id
        self.p_name = p_name
        self.p_loc = p_loc
        self._p_adhaar = p_adhaar # Not supposed to be disclosed

    def showPersonDetails(self, adhaar):

        if adhaar == self._p_adhaar:

            print(": PATIENT DETAILS :")
            print(f"Patiend id : {self.p_id}")
            print(f"Patient name : {self.p_name}")
            print(f"Patient location : {self.p_loc}")
            print("="*50)
            
        else:

            raise ValueError("Adhaar does not matched properly.\n Please enter correct adhaar ID :")

class DiseaseInfo(Person):

    def __init__(self, p_id, p_name, p_loc, p_adhaar, d_name, d_type, sev_lev, diag_date, cur_state):
        super().__init__(p_id, p_name, p_loc, p_adhaar)

        self.d_name = d_name
        self.d_type = d_type
        self.sev_lev = sev_lev
        self.diag_date = diag_date
        self.cur_state = cur_state
        
    def showDiseaseDetails(self, adhaar):

        if adhaar == self._p_adhaar:

            print(": DISEASE DETAILS :")
            print(f"disease name : {self.d_name}")
            print(f"Disease type : {self.d_type}")
            print(f"Severity level : {self.sev_lev}")
            print(f"Diagnosis date : {self.diag_date}")
            print(f"Current state : {self.cur_state}")
            print("="*50)

        else:

            raise ValueError("Adhaar does not matched properly.\n Please enter correct adhaar ID :")

class InPatient(DiseaseInfo):

    def __init__(self, p_id, p_name, p_loc, p_adhaar, d_name, d_type, sev_lev, diag_date, cur_state, room_num, adm_date):
        super().__init__(p_id, p_name, p_loc, p_adhaar, d_name, d_type, sev_lev, diag_date, cur_state)

        self.room_num = room_num
        self.adm_date = adm_date

    def showInPatientDetails(self, adhaar):

        if adhaar == self._p_adhaar:

            print(": IN PATIENT DETAILS :")
            print(f"Room number : {self.room_num}")
            print(f"Admission date : {self.adm_date}")
            print("="*50)

        else:

            raise ValueError("Adhaar does not matched properly.\n Please enter correct adhaar ID :")
    
InP = InPatient(1, "Alex", "London", 1234567, "Dengue", "Viral", "Mild", "2026-01-15", "Active", 200, "2026-01-15")
print(InP.subject)
InP.showPersonDetails(1234567)
InP.showDiseaseDetails(1234567)
InP.showInPatientDetails(1234567)