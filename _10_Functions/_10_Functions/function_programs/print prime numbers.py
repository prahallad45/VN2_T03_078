'''
# print prime numbers using functions
Topics
CRUD Retrieve
Data number
state input number
Behaviour print prime number

'''
print("using functions approach")

x, y = [int(i) for i in input("enter two numbers with min and max range:").split(',')]

while x <= y:
    counter = 0
    i = 2
    while i <= x/2:
        if x % i == 0:
            counter += 1
            break
        i += 1
    if counter == 0 and x != 1:
        print("%d" % x, end=',')
    x += 1


for i in range(30):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)




