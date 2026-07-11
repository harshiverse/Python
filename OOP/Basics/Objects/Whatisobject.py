#object - A "Bundle" of related attributes (variables) [what they have] and methods (functions) [what they can do]
#       - Real-world objects = Phone (attribute = color, model,price), cup(temp, _isempty), book(name, pages)
#       - You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

from car import Car #we are importing the class named "car" from another file

car1 = Car("Lamborgini", 2026, "Golden", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("charger", 2024, "white", True)

print(car1)
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

print(car2)
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

print(car3)
print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)

print(car1.stop)
print(car3.drive)

car1.stop()
car2.stop()
car3.drive()

car1.describe()
car2.describe()
car3.describe()


