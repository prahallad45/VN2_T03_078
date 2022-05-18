# syntax of lambda, map, filter, reduce
'''
lambda
x = 10, y = 25
result = lambda x, y: x + y
print("sum of list:", result(10,5))
result = lambda x: x*x
print("square :" result(5))

map returns list with result elements
list1
list2
print("sum using map:", list(map(lambda x,y: x+y, list1, list2)

filter:returns list with even numbers/ odd
list1
print("filter even numbers:", list(filter(is_even,list1))
print("filter even numbers:", list(filter(lambda x: x%2 == 0, list1))

from functools import reduce: returns single value of entire list after operation
list
print("sum:", reduce(lambda x,y: x+y, list)

'''



# type 1 :with parameters and with return type


def multiply(n1, n2):
    result = n1 * n2
    return result


output = multiply(6, 10)
print("multiply of two numbers s:", output)


# type 2: with parameters and without return type


def divide(x, y):
    result = x / y
    print("division of two numbers is:", result)


print("function calling:", divide(50, 5))

# type 3: with out parameters and with return type


def modulus():
    n1 = 10
    n2 = 6
    result = n1 % n2
    return result


output = modulus()
print("modulus of two numbers:", output)

# type 4: without parameters and without return type


def add():
    n1 = 500
    n2 = 120
    result = n1 + n2


add()
print("sum of two numbers:", add())

# multipliaction functionality
# type1  wp wr


def multiply(n1, n2):
    result = n1 * n2
    return result


output = multiply(100, 25)
print("multiplication of two numbers is:", output)

# type 2  wp & wor


def multiply(n1, n2):
    result = n1 * n2
    print("multiply of two numbers is ", result)


print("function calling:", multiply(50, 96))

# type 3 wop & wr


def multiply():
    n1 = 63
    n2 = 65
    result = n1 * n2
    return result


output = multiply()
print("multiply of two numbers:", output)


# type 4 wop & wor


def multiply():
    n1 = 256
    n2 = -963
    result = n1 * n2
    print("multiply of two numbers:", result)


multiply()
print("function calling", multiply())


# different passing arguments
'''
1. positional arguments (required)
2. default arguments
3. keyword arguments (named)
'''
# 1. positional arguments  : it required values for each arguments neither less nor more


def sum(n1, n2, n3):
    result = (n1 + n2 + n3)
    print("sum of 3 numbers :", result)


sum(10, 50, 689)
sum(10, 5, 96)
sum(10, 86, 96,)


# default arguments : if you assign value to n3 argument it will take or otherwise go with default value

def sum(n1, n2, n3=500):
    result = (n1 + n2 + n3)
    print("sum of 3 numbers:", result)


sum(20, 50)
sum(10, 50, 100)
# sum(10)  error missing n2 argument

# if assign two arguments with values


def sum(n1, n2=45, n3=56):
    result = (n1 + n2 + n3)
    return result


print("one argument:", sum(1))
print("two arguments:", sum(1, 10))
print("three arguments:", sum(50, 65, 86))


'''
def sum(n1=5, n2, n3=65)
    result = (n1+n2+n3)
    print("sum of three numbers", result)
'''

# function overloading : assign values from end

# 3. keyword arguments / named arguments


def sum(n1, n2, n3):
    result = (n1 + n2 + n3)
    print("sum of 3 numbers:", result)


sum(10, 50, 96)  # positional
sum(n1=10, n2=56, n3=60)  # keyword


def get_order_info(flightno, ticketno, gateno, mobileno, destination):
    print("traveller deatails")
    print(flightno, ticketno, mobileno, destination, gateno)


get_order_info(12345, 96566, 2, 965225648, 10)
get_order_info(flightno=12545, ticketno=96566, gateno=2, mobileno=965225648, destination=10)


def get_student_marks(m1, c, wre, hmm, sa, sm):
    print("student marks:")
    print(m1, sa, sm, wre, hmm, c)


get_student_marks(56, 62, 36, 45, 39, 54)
get_student_marks(99, 79, 85, 36, 45, 96)


# positional (n1, n2, n3) = (10, 20, 30)
def add(n1, n2, n3):
    result = (n1+n2+n3)
    print("sum of numbers", result)


sum(10, 20, 30)

# default arguments: (n1, n2, n3=100) assign n1, n2 values


def sum(n1, n2, n3=56):
    result = (n1 + n2 + n3)
    print("sum of numbers:", result)


sum(10, 20)
sum(10, 56, 89)

# keyword arguments : named arguments


def get_movie_ticket_details(movie_name, screen_no, time, date, seat_no):
    print("movie ticket details:")
    print(movie_name, seat_no, time, date, screen_no)


get_movie_ticket_details("paagal", 1, 11.30, "18-aug-2021", "L56")


# lambda function used for makes code simplier

def sum(n1, n2):
    result = (n1 + n2)
    print("sum of two numbers:", result)


sum(10, 20)


sum = lambda n1, n2, n3, x, y: n1 + n2 + n3 + x + y
print("using lambda sum of numbers:", sum(10, 50, 5, 6, 9))

sub = lambda n1, n2: n1 - n2
print("using lambda difference of two numbers:", sub(50, -96))

multiply = lambda n1, n2, n3: n1 * n2 * n3
print("multiply of 3 numbers:", multiply(5, 10, 96))

divide = lambda n1, n2: n1/n2
print("division of two numbers:", divide(10, 5))

modulus = lambda n1, n2: n1 % n2
print("modulus of two numbers:", modulus(100, 6))

cube = lambda n: n*n*n
print("cube of number", cube(250))

# using filter : filter out the even


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


lst = [10, 23, 45, 46, 70, 99]
lst1 = list(filter(is_even, lst))
print(lst1)
lst2 = [0, 1, 2, 3, 5, 5, 6, 8]
lst2 = list(filter(is_even, lst2))
print(lst2)

tup1 = (123, 158, 196, 200, 159)
tup1 = tuple(filter(is_even, tup1))
print(tup1)


def is_odd(x):
    if x % 2 != 0:
        return True
    else:
        return False


set1 = {154, 896, 1543, 156}
set1 = set(filter(is_odd, set1))
print(set1)


# map function: format = map(function, sequence)

def square(x):
    square = x*x
    print("square of a number", square)


square(5)


y = lambda x: x*x
print("square of a number:", y(10))


def squares(x):
    squares = x*x
    return x*x


lst1 = [5, 89, 46]
list1 = list(map(squares, lst1))
print("squares of list1:", list1)


def cubes(x):
    cubes = x*x*x
    return x*x*x


tup = (12, 15, 16, 78)
tup1 = tuple(map(cubes, tup))
print("cubes of tup:", tup1)

tup2 = tuple(filter(is_even, tup1))
print(tup2)

# product of two elements using map functions

list1 = [1, 5, 9, 6]
list2 = [5, 89, 12, 56]
list3 = list(map(lambda x, y: x*y, list1, list2))
print("product of two lists:", list3)

set1 = {15, 19, 23}
set2 = {20, 22, 24}
set3 = set(map(lambda x, y: x * y, set1, set2))
print("product of sets:", set3)


def cubes(x):
    cubes = x*x*x
    return cubes


list1 = [5, 8, 9]
list2 = list(map(cubes, list1))
print(list2)


# reduce function a sequence of elements into single value
from functools import reduce
list1 = [5, 7, 8, 9, 12, 9]
result = reduce((lambda x, y: x*y), list1)
print("product f all elements in list1", result)

tup = (1, 5, 8, 78, 9)
tuple1 = reduce((lambda x, y: x + y), tup)
print("sum of all elements:", tuple1)


def sum(n1, n2):         # function signature
    result = n1 + n2     # function body
    print("sum of two numbers:", result)


sum(10, 96)         # function calling/ invocation

# reurn type


def sum(n1, n2):       # parmeters
    result = n1 + n2
    return result


print("sum of two numbers:", sum(102, 150))  # arguments

# different types of arguments
# 1. positional


def sum(n1, n2, n3):
    result = n1+n2+n3
    return result


print("sum of all numbers", sum(10, 5, 6))


# deault arguments


def sum(n1, n2, n3=100):
    result = n1+n2+n3
    print("sum of numbers:", result)


sum(10, 20)

# 3. keyword arguments (named)


def get_bus_ticket(name, age, origin, destination, date, time, seatno, type):
    print("bus ticket details:")
    print(name, age, origin, destination, date, time, seatno, type)


get_bus_ticket("mani", 26, "HYD", "ATP", "18aug2021", 56, 10.30, "SL")

# ananymous function

# lambda
square = lambda x: x*x
print("square of", square(9))
# filter
lst1 = [12, 5, 7, 8, 9]

print("filter even numbers:", list(filter(is_even, lst1)))
print("filter even numbers:", list(filter(lambda x: x % 2 == 0, lst1)))
print("filter odd numbers:", list(filter(is_odd, lst1)))
print("filter odd numbers:", list(filter(lambda x: x % 2 != 0, lst1)))
# map gives sum product two lists in a list
lst1 = [1, 5, 8, 9]
lst2 = [12, 45, 69, 5]

print("product of two list elements:", list(map(lambda x, y: x * y, lst1, lst2)))
print("sum of two list elements:", list(map(lambda x, y: x + y, lst1, lst2)))
print("division of two list elements:", list(map(lambda x, y: x / y, lst1, lst2)))

# reduce gives the final result of entire list elements


from functools import reduce

list1 = [1, 5, 6, 9]
print("sum using reduce", reduce(lambda x, y: x + y, list1))

lst1 = [1, 5, 8, 9]
lst2 = [12, 45, 69, 5]
print("product using reduce :", reduce(lambda x, y: x * y, lst1))
print("product using reduce :", reduce(lambda n1, n2: n1*n2, lst2))
