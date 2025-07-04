# collection = single "variable" used to store multiple values
#   List  = [] ordered and changeable. Duplicates Ok
#   Set   = {} unordered and immutable, but Add/Remove Ok, No duplicates
#   Tuple = () ordered and unchangeable. Duplicates Ok. FASTER


# 1) List
# fruits = ["apple", "orange", "banana", "coconut"]

# print(fruits) # ['apple', 'orange', 'banana', 'coconut']
# print(fruits[0]) # apple
# print(fruits[:3]) # ['apple', 'orange', 'banana']
# print(fruits[::2]) # ['apple', 'banana']
# print(fruits[::-1]) # ['coconut', 'banana', 'orange', 'apple']

# for fruit in fruits:
    # print(fruit)
# output
# apple
# orange
# banana
# coconut

# print(dir(fruits)) # It will print all the methods of list
# print(help(fruits)) # it will print all the methods of list with descriptions
# print(len(fruits)) # gives the length of list
# print("pineapple" in fruits) # gives boolean value true or false

# fruits[0] = "pineapple" # list can be change means they are mutable
# if we will print(fruits) it will show like this
# ['pineapple', 'orange', 'banana', 'coconut']

# fruits.append("pineapple") # ['apple', 'orange', 'banana', 'coconut', 'pineapple']
# fruits.remove("apple") # ['orange', 'banana', 'coconut', 'pineapple']
# fruits.insert(0, "pineapple") # ['pineapple', 'apple', 'orange', 'banana', 'coconut']
# fruits.sort() # ['apple', 'banana', 'coconut', 'orange']
# fruits.reverse() # ['coconut', 'banana', 'orange', 'apple']
# fruits.clear() # []
# print(fruits.index("apple")) # 0
# print(fruits.count("apple"))

# print(fruits)

# 2) set

# fruits = {"apple", "orange", "banana", "coconut"}

# print(fruits) # it will show the element but in unordered means every time when
# we run the program it will show different order for same element of set.

# print(dir(fruits)) # It will print all the methods of set
# print(help(fruits)) # it will print all the methods of sets with descriptions
# print(len(fruits)) # gives the length of set
# print("pineapple" in fruits) # gives boolean value true or false

# indexing is not possible here like in list print(fruits[0]) because of unordered
# we can add and remove element

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop() # It will remove any element
# fruits.clear()
# print(fruits)

# 3) tuple

fruits = ("apple", "orange", "banana", "coconut")

# print(dir(fruits)) # It will print all the methods of tuple
# print(help(fruits)) # it will print all the methods of tuple with descriptions
# print(len(fruits)) # gives the length of tuple
# print("pineapple" in fruits) # gives boolean value true or false

# There are two method of tuple

print(fruits.index("apple"))
print(fruits.count("banana"))
print(fruits)

for fruit in fruits:
    print(fruit)


