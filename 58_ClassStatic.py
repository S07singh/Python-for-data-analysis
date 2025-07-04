# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself.

# Instance methods = Best for operations on instances of the class(objects)
# Static methods = Best for utility functions that do not need access to class data
# Class methods = Best for class-level data or require access to the class itself.
class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #INSTANCE METHODS
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count}"


student1 = Student("Sudhir", 9.4)
student2 = Student("Divya", 9.5)
student3 = Student("Gunjan", 9.1)

print(Student.get_count())
print(Student.get_average_gpa())