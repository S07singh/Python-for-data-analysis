# class variables = shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:

    class_year = 2027 # class variable
    num_student = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_student += 1


student1 = Student("Sudhir", 20)
student2 = Student("Gunjan", 20)
student3 = Student("Divya", 20)
student4 = Student("Rahul", 20)

# print(student2.name)
# print(student2.age)
# print(student2.class_year)
# print(Student.class_year) # we can access class variable with className
# if class is in different file then we can tell that which one is
# instance variable and which is class variable, class variable can be access by class name.
print(Student.num_student)

print(f"My graduating class of {Student.class_year} has {Student.num_student} students")