# List comprehension = A concise way to create lists in python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

'''
doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# This is a lot to write so by using list comprehension it can write
# in concise way and more compact easier to read.
'''

'''
doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
square = [z * z for z in range(1, 11)]

print(doubles) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(triples) # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
print(square) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
'''
fruits = ["apple", "orange", "banana", "coconut"]

fruits = [fruit.upper() for fruit in fruits]
# fruits = [fruit.upper() for fruit in ["apple", "orange", "banana", "coconut"]]

print(fruits)  # ['APPLE', 'ORANGE', 'BANANA', 'COCONUT']

fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars) # ['a', 'o', 'b', 'c']

'''

'''
numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_num = [num for num in numbers if num >= 0]
negative_num = [num for num in numbers if num < 0]
even_num = [num for num in numbers if num % 2 == 0]
odd_num = [num for num in numbers if num % 2 != 0]

print(positive_num) # [1, 3, 5, 8]
print(negative_num) # [-2, -4, -6, -7]
print(even_num) # [-2, -4, -6, 8]
print(odd_num) # [1, 3, 5, -7]

'''

grades = [85, 42, 79, 90, 56, 61, 30]

passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades) # [85, 79, 90, 61]


