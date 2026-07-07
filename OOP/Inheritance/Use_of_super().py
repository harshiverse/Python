#super() - Function used in a child class (subclass) to call methods from a parent class (superclass).
#        - Allows you to extend the functionality of the inherited methods.

#------------------Example----------------------

class Circle:
    def __init__ (self, color, filled, radius):
         #In order to intanceate objects we require a constructor
        self.color = color
        self.filled = filled
        self.radius = radius

class Square:
     def __init__ (self, color, filled, width):
         #In order to intanceate objects we require a constructor
        self.color = color
        self.filled = filled
        self.width = width

class Triangle:
     def __init__ (self, color, filled, radius):
         #In order to intanceate objects we require a constructor
        self.color = color
        self.filled = filled
        self.width = width 
        self.height = height 

#------In programming, we try to not repeat ourselves. We would like to keep the code as short and clean as possible. We shall make the code reusable.---------

class Shape:
    def __init__ (self,color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):
    def __init__(self, color, is_filled,radius):
        super().__init__(color, is_filled)
        self.radius = radius
    
class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled) 
        self.width = width

class Triangle(Shape):
    def __init__(self,color,is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle ("red", True, 5) #you can also write color = "red", is_filled = "True", radius = 5 for better readability
square = Square (color = "blue", is_filled = False , width = 4)


print(circle.color)
print(circle.is_filled)
print(circle.radius)
print(f"The radis is {circle.radius}.")

#-------------MY QUESTIONS-------------

#Q1 Why did we use __init__ function in circle, square as well when we already defined it once in Shape?
# Since circle inherits from shape should it able to use the __init__ method functionality automatically?