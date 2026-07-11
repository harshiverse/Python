class Car: #This is a class named "Car"
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self): #This is a method named "drive"
           print("You should drive the car")

    def stop (self):
         print(f"You stop the {self.model}")

    def describe(self):
         print(f"{self.year} {self.color} {self.model}")
         