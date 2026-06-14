class Myclass:
    className = "MyClass"
    
    def sayHello(self, name):
        print(f"Hello,{name}!, I am {self.className}.")
    
    obj = Myclass()
    obj.sayHello("Harshita") #Hello,Harshita, I am MyClass.
    
    print(type(obj.sayHello("Harshita")))
    
    class calculator:
        
        def add(self,x,y):
            return x+y
        def subtract(self,x,y):
            return x-y
        def multiply(self,x,y):
            return x*y
        def divide(self,x,y):
            if y !=0:
                return x/y
            else:
                return "Cannot divide by zero"
            
        calc = Calculator() 
        print(calc.add(5,3))
            
        class Student:
            
            def __init__(self,name,grade,admissionNumber):
                self.name = name
                self.grade = grade
                self.admissionNumber = admissionNumber
                
            def is_passing(self):
                return self.grade >= 60
                
            def details(self):
                return f"{self.name} (Admission Number: {self.admissionNumber}) has a grade of {self.grade}"
                
            student1 = Student("Harshita", 0, "ddcdf")
            student2 = Student("Avi", 70, "eefef")
            print(student1.is_passing())
            print(student2.is_passing())
            
            print(student1.details())
            print(student2.details())
            
    class encapsulationDemo:
        
        def __init__(self, value):
            self.__private_value = value
            
            def get_value(self):
                return self.__private_value
            def set_value(self):
                if new_value >= 0:
                   self.__private_value = new_value
                
demo = encapsulationDemo(10)
print(demo.get_value())
demo.set_value(20)
print(demo.get_value())
    
class areaCalculator:
        
    def areaOfCircle(self,r):
        area= 3.14* r**2
        return area
            
    def areaOfRectangle(self, 1, b):
        area = 1*b
        return area
            
calc = areaCalculator()
print(calc.areaOfCircle(5))

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
class Polymorphism()

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"
    
class Bike(Vehicle):
    def start_engine(self):
        return "Bike engine started"