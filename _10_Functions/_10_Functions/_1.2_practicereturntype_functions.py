


def add(n1, n2):   # without return type
    result = n1 + n2
    print("sum of two numbers:", result)


add(10, 20)
print("function call:", add(100, 200))


def sub(n1, n2):
    result = n1 - n2
    print("subtraction of two numbers:", result)


sub(100, 110)
sub(500, 350)
print("function calling:", sub(100, 110))


# with return type

def add(n1, n2):
    result = n1 + n2
    return result


output = add(100, 50)
print("return result:", output)
output = add(-50, -96)
print("return result:", output)


def sub(n1, n2):
    result = n1 - n2
    return result


output = sub(150, 65)
print("function calling:", output)

list1 = [156, -100, 96, "a"]
print("after append the list:", list1.append(9))
append_item = list1.append(105)
print("after append value with return:", append_item)
print("after append the list:", list1)

print("after removing:", list1.remove(96))
val = list1.remove(-100)
print("after removing -100", val)
print("after removing items:", list1)

# with return functions
print("after popping: ", list1.pop())
print("after popping:", list1.pop())
print("after popping:", list1.pop())
print("after popping:", list1)

print("after indexing :", list1.index(156))
print("after indexing:", list1.index(156))
print("list items:", list1)


# return type functions

n1 = int(input("Enter first number is:"))
n2 = int(input("Enter second number is:"))


def sub(x, y):
    result = n1 - n2
    return result


output = sub(n1, n2)
print("differnce of two numbers is :", output)
