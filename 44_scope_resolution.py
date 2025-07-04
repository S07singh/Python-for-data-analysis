# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

'''
# local
def fun1():
    x = 1
    print(x)


def fun2():
    x = 2
    print(x)

fun2()
fun1()
'''

'''
# enclosed
def fun1():
    x = 1
    def fun2():
        # x = 2
        print(x) # if local variable x = 2 is not present in fun2 then 
        # it will use x = 1 enclosed variable(function inside a function)
    fun2()

fun1()
'''
'''
# Global 
# if local variable is not present, then it will use global
# A variable defined outside of function is global variable
def fun1():
    # x = 1
    print(x)
def fun2():
    # x = 2
    print(x)

x = 3

fun2()
fun1()
'''

# built-in
from math import e


def func1():
    print(e)

# e = 3 # global
func1()