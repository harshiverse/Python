#Static Methods - A method that belong to a class rather than any object from that class (instance).
#               - Usually used for general utility functions

# Instance Method - Best for operations on instances of the class (objects)
# Static Method - Best for utility functions that do not need access to class data

class Employee:
    def __init__(self, name, job_title):
          self.name = name
          self.jobtitle = job_title

    def get_info(self):
         return f"{self.name} = {self.jobtitle}"

    @staticmethod
    def is_valid_title(job_title):
         valid_title = ["Manager", "Cashier", "Cook", "Janitor"]
         return job_title in valid_title
    
employee1 = Employee("Ria","Manager") #object for instance method...static method do not require objects
employee2 = Employee("Sia", "Cashier")
employee3 = Employee("Pia", "Cook")

print(Employee.is_valid_title("Janitor"))#static method
print(employee1.get_info()) #instance method
print(employee2.get_info())
print(employee3.get_info())
