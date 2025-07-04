# Exercise 1 Area of rectangle
length = int(input("Length of rectangle: "))
width = int(input("width of rectangle: "))

area = length * width
print(f"The area of rectangle is {area} cm²")

# Exercise 2 Shopping cart program
item = input("what item would you like to buy ?: ")
price = float(input(f"what is the price of each {item} ?: "))
quantity = int(input(f"How many {item} would you like to buy ?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s ")
print(f"Your total is: ${total}")