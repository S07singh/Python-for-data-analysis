# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop


# list & tuple
# numbers = [1, 2, 3, 4, 5]
numbers = (1, 2, 3, 4, 5)  # tuple

# for number in reversed(numbers):
#     print(number, end=" ")


# set
fruits = {"apple", "orange", "banana", "coconut"}

# for fruit in fruits: # set is not reversible bcz it not in the order
#     print(fruit)


# string
name = "Sudhir Singh"

# for character in name:
#     print(character, end=" ")


# dictionary
my_dictionary = {"A": 1, "B": 2, "C": 3}
# for key in my_dictionary.keys():
# for key in my_dictionary: # same for key
#     print(key)

# for value in my_dictionary.values(): # for value
#     print(value)

for key, value in my_dictionary.items():
    print(f"{key}:{value}")
