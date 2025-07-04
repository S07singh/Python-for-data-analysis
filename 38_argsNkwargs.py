# *args      = allow you to pass multiple non-key arguments
# **kwargs   = allow you to pass keyword arguments
#              * unpacking operator
#              1. positional, 2. default, 3. KEYWORD, 4. arbitrary

def add(*args):  # type of 8args is tuple, here args become tuple means any number of argument it can take
    total = 0
    for arg in args:
        total += arg
    return total


# print(add(1, 2, 3, 4, 5, 6))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")


# display_name("Dr.", "Spongebob", "Harold", "Square pants", "III")


def print_address(**kwargs):  # type of **kwargs is dictionary
    # for value in kwargs.values():
    #     print(value)

    # for key in kwargs.keys():
    #     print(key)

    for key, value in kwargs.items():
        print(f"{key}:{value}")


# print_address(street="123 Fake St.",
#               apt="100",
#               city="Detroit",
#               state="MI",
#               zip="54321")


# Exercise
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    # for value in kwargs.values():
    #     print(value, end=" ")

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")


shipping_label("Dr.", "Spongebob", "Harold", "Square pants", "III",
               street="123 Fake St.",
               # apt="#100",
               pobox="PO box #1001",
               city="Detroit",
               state="MI",
               zip="54321")
