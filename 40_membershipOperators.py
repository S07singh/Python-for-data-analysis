# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                         1. in
#                         2. not in


# 1.) string
'''
# (a) in
word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")
'''

'''
# (b) not in
word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter not in word:
    print(f"{letter} was not found")
else:
    print(f"There is a {letter}")
'''


# 2.) set, list, tuple
''' 
# (a) in
students = {"sudhir", "divya", "rahul"}

student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not student")
'''

'''
# (b) not in
students = {"sudhir", "divya", "rahul"}

student = input("Enter the name of a student: ")

if student not in students:
    print(f"{student} was not student")
else:
    print(f"{student} is a student")
    
'''

# 3) dictionary
# (a) in
'''
grades = {"Sudhir": "A",
          "Divya": "B",
          "Gunjan": "C",
          "Anjali": "D",
          "Sunil": "E"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")

'''

# Example
email = "sudhirsingh@gmail.com"

if '@' in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")


