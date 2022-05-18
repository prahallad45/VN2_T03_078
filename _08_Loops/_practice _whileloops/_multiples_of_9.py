# using while loop print first 5 multiples of 9
n1, n2 = [int(i) for i in input("enter two numbers in minimum and maximum range :").split(',')]

counter = 0
while n1 <= n2:
    if n1 % 9 == 0:
        print(n1)
        counter += 1
        if counter == 5:
            break
    n1 += 1
