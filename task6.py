class Hospital:
    def __int__(self, admin, doctor, nurse, dpt):
        self.admin = admin
        self.doctor = doctor
        self.nurse = nurse
        self.dpt = dpt

    def get_info(self):
        print("Hospital details")
        self.admin = input("Enter admin name:")
        self.doctor = input("Enter the doctor's name:")
        self.nurse = input("Enter the nurse name:")
        self.dpt = input("Enter the department:")

class Department(Hospital):
    def details(self):
        print("\n""Hospital details")
        print("Admin:", self.admin, "\n""Doctor:", self.doctor, "\n""Nurse:", self.nurse, "\n""Department:", self.dpt)


class Patientward(Department):
    def __int__(self, name, age, number, disease):
        self.name = name
        self.age = age
        self.number = number
        self.disease = disease

    def getdetails(self):
        print("Patient details")
        self.name = input("Enter the name:")
        self.age = int(input("Enter the age:"))
        self.number = int(input("Enter the number:"))
        self.disease = input("Enter the disease:")

    def putdetails(self):
        print("\n""Patient details:")
        print("Patient name:", self.name, "\n""Age:", self.age, "\n""Number:", self.number, "\n""Disease:",
              self.disease)


obj1 = Hospital()
obj2 = Patientward()
obj2.get_info()
obj2.getdetails()
obj2.details()
obj2.putdetails()
