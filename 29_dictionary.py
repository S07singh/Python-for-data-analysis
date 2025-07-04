# Dictionary = a collection of {key: value} pairs
#               ordered and changeable. No duplicates


capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("India"))

# if capitals.get("Russia"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"}) # it will insert new element
# capitals.update({"USA": "Detroit"}) # it will update the existing element value
# capitals.pop("China")
# capitals.popitem() # it doesn't require input it will remove the latest element from dictionary
# capitals.clear()

# print(capitals)

# keys = capitals.keys() # it will return keys of dictionary
# print(keys) # dict_keys(['USA', 'India', 'China', 'Russia'])

# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# print(values) # dict_values(['Washington D.C.', 'New Delhi', 'Beijing', 'Moscow'])

# for value in capitals.values():
#     print(value)

# items = capitals.items()
# print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")
