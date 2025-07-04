# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reuseable separate files

# help("modules")
# print(help("math"))

# import math
# import math as m
# from math import pi
# from math import e

# print(math.pi)
# print(m.pi)
# print(pi)

# a, b, c, d, e = 1, 2, 3, 4, 5
# print(math.e ** a)
# print(math.e ** b)
# print(math.e ** c)
# print(math.e ** d)
# print(math.e ** e)

import example

result = example.pi
result = example.square(3)
result = example.cube(3)
result = example.circumference(3)
result = example.area(3)

print(result)


