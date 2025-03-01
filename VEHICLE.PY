class bmw():
    def fueltype(self):
        print("BMW FUEL TYPE: petrol, diesel, electric")
 
    def maxspeed(self):
        print("BMW MAX SPEED:250 km/h")
class ferrari():
    def fueltype(self):
        print("FERRARI FUEL TYPE:petrol")
 
    def maxspeed(self):
        print("FERRARAI MAX SPEED:340 km/h")

 

obj1 = bmw()
obj2 = ferrari()

# Common Interface
for car in (obj1, obj2):
    car.fueltype()
    car.maxspeed()