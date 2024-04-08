# Kesny Raingsey
# SDEV220
# 4/08/2024
# M03 Lab - Case Study.py

#Write an app that will accept user input for a car. The app will store "car" into the vehicle type in your Vehicle super class
#A super class called Vehicle, which contains an attribute for vehicle type, such as car, truck, plane, boat, or a broomstick
class Vehicle:
    def __int__(self, vehicle_type):
        self.vehicle_type = vehicle_type

 #A class called Automobile which will inherit the attributes from Vehicle and also contain the following attributes: year, make, model, doors (2 or 4), roof (solid or sun roof).   
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    
    def displayInfo(self):
        print("Vehicle type: car")
        print("Year: ",self.year)
        print("Make: ",self.make)
        print("Model: ",self.model)
        print("Number of doors:", self.roof)
 
 ##The app will then ask the user for the year, make, model, doors, and type of roof and store thdata in the attributes above   
year1 = int(input("Enter the car year: "))
make1 = input("Enter the car make: ")
model1 = input("Enter the car model: ")
doors1 = int(input("Enter the number of the car doors(2 or 4): "))
roof1 = input("Enter the type of roof(solid or sun roof): ")
Car = Automobile(year1, make1, model1, doors1, roof1)
Car.displayInfo()

