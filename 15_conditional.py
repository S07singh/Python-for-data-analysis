# Conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          print or assign one of two values based on a condition
#                          X if condition else Y

num = 4
a = 6
b = 2
age = 20
temperature = 25
user_role = "admin"

print("Positive" if num > 0 else "Negative")
result = "Even" if num % 2 == 0 else "OOD"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Child"
weather = "HOT" if temperature > 20 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(result)
print(max_num)
print(min_num)
print(status)
print(weather)
print(access_level)