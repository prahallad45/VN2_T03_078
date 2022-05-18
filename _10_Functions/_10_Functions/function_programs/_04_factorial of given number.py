'''

# find the factorial of given number

Topics
CRUD - retrieve
Data - number
state - input nummber
behaviour - factorial of given number

'''

num = int(input("Enter the number:"))

def factorial(num):
    result = 1 if (num == 0 or num == 1) else num*factorial(num-1)
    return result

print("factotial of inut number:" ,factorial(num))


