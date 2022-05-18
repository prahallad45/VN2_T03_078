# Display odd numbers in range of MINIMUM AND MAXIMUM of any two numbers
a, b = [int(i) for i in (input("enter any two numbers in range of minimum and maximum :").split(','))]
while a <= b:
    if a % 2 == 1:
        print(a)
    a += 1

# Display first 10 odd numbers using while loop and break statement

x, y = [int(i) for i in input("Enter two numbers of minimum and maximum range :").split(',')]

counter = 0
while x <= y:
    if x % 2 == 1:
        print(x)
        counter += 1
        if counter == 10:
            break
    x += 1

# Diplay odd numbers using while and continue

m, n = [int(i) for i in input("Enter two numbers :").split(',')]
counter = 0
while m < n:
    m += 1
    if m % 2 == 1:
        counter += 1
        if counter == 8:
            continue
        print(m)

# using while and continue
c = int(input("Enter minimum number :"))
d = int(input("Enter maximum number :"))
counter = 0
while c < d:
    c += 1
    if c % 2 == 1:
        counter += 1
        if counter == 10:
            continue
        print(c)

