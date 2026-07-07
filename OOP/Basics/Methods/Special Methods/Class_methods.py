#Class methods - Allos operations related to class itself
#              - Take (cls) as the first parameter, hich represents class itself.

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

     #INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    
    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa/ cls.count}"

student1 = Student("Spongebob", 4.5)
student2 = Student("Sandy", 3.1)
student3 = Student("Patrik", 2.4)

print(Student.get_count())
print(Student.get_avg_gpa())
