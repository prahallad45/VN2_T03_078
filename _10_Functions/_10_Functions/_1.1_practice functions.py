def add(n1, n2):       # parameters, function signature
    result = n1 + n2       # business logic, function body
    print("addition is:", result)
# function calling


add(10, 20)    # arguments
add(-15, 30)
add(-2, 10)
add(55, 60)
add(0, 5)


def sub(n3, n4):
    result = n3 - n4
    print("sub is :", result)


sub(40, 20  )
sub(-10, -40)
sub(-5, -6)
sub(-16, 0)
sub(-1, 62)


def multiply(n1, n2):
    result = n1 * n2
    print("multiplication of two numbers:", result)


multiply(15, 20)
multiply(-5, 20)
multiply(2, 156)
multiply(156, 200)
multiply(256, -196)


def division(n1, n2):
    result = n1 / n2
    print("division of two numbers:", result)


division(15, 3)
division(-5, 3)
division(-65, 6)
division(-9, 6)


def modulus(n1, n2):
    result = n1 % n2
    print("modulus of two numbers is :", result)


modulus(10, 56)
modulus(0, 5)
modulus(-1, 2)
modulus(-56, 5)
modulus(-96, -36)


def floor_division(n1, n2):
    result = n1 // n2
    print("floor division of two numbers:", result)


floor_division(12, 56)
floor_division(12, 3)
floor_division(-56, 4)

# state = input of customer given
# behaviour = sum function

# advantages : code duplication is not done, reuseability,Need to change code only at once


def add(n1, n2):
    result = n1 + n2
    print("sum of two numbers is:", result)


add(1, -80)
add(56, 86)
add(95, 205)
'''
# Types of functions
# 1.Builtin functions = print(), id(), Type(), len() and which are in python lib
# 2. user defined functions = functions which are defined by user/ programmer

x = 10
x - variable/ identifier
= - assignment operator
10 - value/ literal


# without functions:

1. state 
n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))

2. behaviour
result = n1 + n2
print("sum of two numbers:", result)

'''
# using functions
'''
1. state
n1 = int(input)             n1, n2 are variables
n2 = int(input)

2.Behaviour:
def add(n1, n2)                            function signature      n1, n2 are parameters
    result = n1 + n2                       function body
    print("sum of two numbers is:", result)
    

add(6, 10)                                  function calling/invocation        6, 10 are arguments      
    
    
'''
