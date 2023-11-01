class Student:
    def __int__(self,name,mark):
        self.name=name
        self.mark=mark
    def getdetails(self):
        self.name=input("Enter the name:")
        self.mark=int(input("Enter you mark:"))
    def putdetails(self):
        print(self.name,self.mark)
class teacher():
    def display(self):
        print("i am derived class")
class parent(teacher,Student):
    def funparent(self):
        print("i am parent class")
obj=parent()
obj.getdetails()
obj.putdetails()
obj.display()
obj.funparent()
