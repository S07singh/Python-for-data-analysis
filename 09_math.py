import math

print(math.sqrt(25))  # 5.0

print(math.pow(2,3))  # 8.0

print(math.floor(3.7))  # 3

print(math.ceil(3.1))  # 4

print(math.factorial(5))  # 120

print(math.gcd(12, 18))  # 6

print(math.pi)  # 3.141592653589793
print(math.e)   # 2.718281828459045

print(math.sin(math.pi / 2))  # 1.0


# Exercise
radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)

print(f"The circumference of circle is {round(circumference, 2)}cm")
print(f"The area of a circle is {round(area, 2)}cm²")

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side C = {round(c,2)}")