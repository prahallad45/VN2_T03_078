x, y = [int(i) for i in input("enter two numbers :").split(',')]
while x <= y:
    if x % 2 != 0 and x % 3 != 0 and x % 4 != 0 and x % 5 != 0:
        if x % 6 != 0 and x % 7 != 0 and x % 8 != 0 and x % 9 != 0:

            print(x)
    x += 1

x, y = [int(i) for i in (input("Enter two  number ;").split(','))]

while x <= y:
    counter = 0
    i = 2
    while i <= x/2:
        if x % i == 0:
            counter += 1
            break
        i = i + 1
    if counter == 0 and x != 1:
        print("%d" % x, end=' ')
    x += 1
