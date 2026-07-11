#Encapsulation - Encapsulation is one of the key features of object-oriented programming.
#              - Encapsulation refers to the bundling of attributes and methods inside a single class.
#              - prevents outer classes from accessing and changing attributes and methods of a class.
#              - helps in data hiding (you do not know what medicine is there in the capsule i.e Encapsulation (wrapping ot bundling of data))
#              - important for security


#In python, we denote private attributes using underscore as the prefix i.e. single (_) or double (__)


class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}". format(self.__maxprice))

    def setMaxprice(self, price):
        self.__maxprice = price

comp1 = Computer()
comp1.sell()
comp1.__maxprice = 1000 #it is a private method can not be accessed directly that is ntg changes
comp1.sell()
comp1.setMaxprice(1000)
comp1.sell()
comp1.setMaxprice(3000)
comp1.sell()


def __init__(self,name,age,gender):
    self.__name = name
    self.__age = age
    self.__gender = gender
    
@property
def Name(self):
    return self.__name

@Name.setter
def Name(self, value):
      self.__name = value

p1 = Person ("ria", 20, 'f')
print(p1.Name)

