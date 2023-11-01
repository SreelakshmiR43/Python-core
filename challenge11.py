class Vehicles:
    def __init__(self,model,year,fueltype,color):
        self.model = model
        self.year= year
        self.fueltype=fueltype
        self.color = color

    def getspecs(self):
        self.model = input("Model:")
        self.year = int(input("Year:"))
        self.fueltype=input("Fuel Type:")
        self.color = input("Color:")

    def displayspecs(self):
        print("\nModel of the vehicle:",self.model,"\nYear:",self.year,"\nFuel Type:",self.fueltype ,"\nColor of the vehicle:",self.color)



class Car(Vehicles):
    def __int__(self,seating_capacity):
        self.seating_capacity=seating_capacity
    def getcarspecs(self):
        self.seating_capacity = int(input("enter the number of seats in car:"))
    def putcarspecs(self):
        print("Number of seats in the car:",self.seating_capacity)


class Bike(Vehicles):
    def __int__(self,wheels):
        self.wheels=wheels
    def getbikespecs(self):
        self.wheels = int(input("enter the number of wheels in bike:"))
    def putbikespecs(self):
        print("Number of wheels in bike:",self.wheels)

obj = Car('','','','')
obj.getspecs()
obj.getcarspecs()
obj.displayspecs()
obj.putcarspecs()

