# using while ,numbers which are divisible by 5 between any two nummbers

x = int(input("Enter first number :"))
y = int(input("Enter second number :"))

while x <= y:
    if x % 5 == 0:
        print(x)
    x += 1
print("End of the Program")


