# if = Do some Code IF some condition is true
#     Else do something else

age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("you are now signed up")
elif age < 0:
    print("you are not born yet!")
else:
    print("you must be 18+ to sign up")

response = input("Would you like food?? (Y/N)")

if response == "Y":
    print("Have some food")
else:
    print("No food for you")

name = input("Enter your name: ")

if name == "":
    print("You dickhead type your name motherfucker!")
else:
    print(f"Your name is {name}")

for_sale = True

if for_sale:
    print("This item is for sale!")
else:
    print("This item is NOT for sale!")

online = False

if online:
    print("You are online now")
else:
    print("You are not online now!")
