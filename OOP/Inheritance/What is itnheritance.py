#Inheritance - Allows a class to inherit attributes and methods from another class
#            - Helps with code reusability and extensibility
#            - Class Clild (Parent)
#            - use less no. of lines in code. hence, improving readability
#            -without inheritance, if u have to make a change then u will have to make the change on all the classes.
#            -with inheritance,one change to parent automatically changes the child classes. (good for when u have alot of classes)

class Animal: #This is the parent class named Animal which inherets properties to child classes(dog,cat,mouse)
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating") 

    def sleep(self):
        print(f"{self.name} is sleeping") #I can change it to is asleep and the change will made for all the child classes(dog,cat,mouse)

class Dog(Animal): #This is a child class named dog which inherets properties from parent class (Animal)
    def bark(self): #Each child class can have their own respective methods as well
        print("WOOF!")

class Cat(Animal): #Another child class
    def meow(self):
        print("MEOW!")
    
         
class Mouse(Animal): #Another child class
    def squeek(self):
        print("SQUEEK!")
         
dog = Dog("Scooby")
cat = Cat("GArfield")
mouse = Mouse("Mickey")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()

print(mouse.name)
print(mouse.is_alive)
mouse.eat()
mouse.sleep()

#Testing their different methods
#dog.speak()
#cat.speak()
#mouse.speak()

#Works even with different method names
dog.bark()
cat.meow()
mouse.squeek()

#-------------------------MY QUESTIONS------------------------------

#Q1 Why did dog.name had to be printed but dog.eat was displayed without printing? Don't we need to print something to display it?