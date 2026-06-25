# "Multiple inheritance" - inherits from more than one parent class
# C(A,B) - a child class C can inherit properties from both class A and B   
# In python, you can have more than one parent

# "Multi-level inheritance" - inherit from a parent which inherits from another parent
# C(B) <- B(A)  <- A -- Here, C inherits from B and B inherits from A.

#--------------Multiple Inheritance----------------
class Prey:
    def flee(self):
        print("This animal is fleeing")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey): #Rabbit(often a prey) will inherit the prey class and gets access to flee method
    pass

class Hawk(Predator): #Hawk (a predator) inherits from predator class.
    pass

class Fish(Prey, Predator): #Bigger fishes eat smaller fishes. Fishes get access to both prey and predator class.
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee() #rabbit should have a flee method
#rabbit.hunt() #gives an error "'Rabbit' has no attribute 'hunt'"

hawk.hunt() #hawk can hunt
#hawk.flee() #gives an error

fish.flee()
fish.hunt() # fish inherit from both the classes and can do both flee and hunt


#-------------Multi-level Inheritance---------------
class Animal:
    def eat(self): #All animals need to eat
        print("This animal is eating...")

    def sleep(self):
        print("This animal is sleeping...")

class Preyy(Animal):
    def fleee(self):
        print("This animal is fleeing...")

class Predatorr(Animal):
    def huntt(self):
        print("This animal is hunting...")

class Deer(Preyy):
    pass

class Lion(Predatorr):
    pass

lion = Lion ()
deer = Deer()

deer.eat()
lion.eat()
deer.sleep()
lion.sleep()

#----------------ASSIGNMENT-----------------

# Q. WAP to show multiple and multi-level inheritance. Also, make use of constructor in your program.
