# using while loop print first  15 even numbers between 500 to 1000

a = 500
b = 1000
counter = 0
while a <= b:
    if a % 2 == 0:
        print(a)
        counter += 1
        if counter == 15:
            break
    a += 1

# using while print even numbers between of any two numbers

x, y = [int(i) for i in input("Enter two numbers :").split(',')]
while x <= y:
    if x % 2 == 0:
        print("Even numbers are :", x)
    x += 1

# using while and continue
c = int(input("Enter minimum number :"))
d = int(input("Enter maximum number :"))
counter = 0
while c < d:
    c += 1
    if c % 2 == 0:
        counter += 1
        if counter == 10:
            continue
        print(c)
