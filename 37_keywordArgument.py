# keyword arguments = an arguments preceded by identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional, 2. default, 3. KEYWORD, 4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")


hello("Hello", title="Mr.", last="John", first="James") # Hello Mr.James John
# In this order of argument doesn't matter by using keyword for arguments
# but when there is a positional argument it should be first then the keyword arguments

for x in range(1, 11):
    print(x, end=" ") # end is keyword argument of print function
print()
print("1", "2", "3", "4", "5", sep="-") # sep(separate) is also keyword argument


# exercise

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=91, area=123, first=456, last=7890)

print(phone_num)




