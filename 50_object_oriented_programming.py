# object = A "bundle" of related attributes (variable) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many variables

# class = (blueprint) used to design the structure and layout of an object

from car import Car

''' # move the class in file 'car' and then use
class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
    def drive(self):
        print(f"You drive the {self.color} {self.model}")
    
    def stop(self):
        print(f"You stop the {self.color} {self.model}")
        
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")
'''


car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("charger", 2026, "yellow", True)


print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)

car1.drive()
car2.describe()
car3.stop()