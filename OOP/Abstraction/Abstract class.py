#Abstract class - A class that cannot be intantiated on its own; Meant to be subclassed.
#               - They can contain abstract methods, which are declared but have no implementation.
#               - Prevents instantistion of the class itself
#               - Requires children to use inherited abstract methods

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# vehicle = Vehicle()       #This will give error because the above methods can not be intantiated directly

#class Car(Vehicle):         #This too shall give an error 
#   pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

car = Car()

car.go()
car.stop()

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")

motorcylce = Motorcycle()

motorcycle.go()
motorcycle.stop()


#class Boat(Vehicle):        #This too will give an type error if you forget to define one method. All vehicles should be able to stop and go
#
#    def go(self):
#        print("you sail the boat")
#
#boat = Boat()               


    
