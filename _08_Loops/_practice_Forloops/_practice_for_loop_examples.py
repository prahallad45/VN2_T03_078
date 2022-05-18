# example 1
str = "hello"

for ch in str:
    print("characters :", ch)

# example 2

str = "welcome"
n = len(str)
for i in range(n):
    print(str[i])

# display odd numbers

for i in range(1, 10, 2):
    print(i)

# display numbers in descending order 10 to 1
for i in range(10, 0, -1):
    print(i)

# display multiples of 11 between 101,150
for x in range(101, 150, 11):
    print(x)

# display elements in list
list =[12.5, 869, "cat", "wolf", "A", "b", 78]

for elements in list:
    print(elements)


# sum of numbers with sum
val = [14, 78, 96, 65, 78]
sum = 0

for i in val:
    print(i)
    sum += i
print("sum = ", sum)

# display squares of numbers
list = [5, 7, 9, 18, 22]
sq = 1
for i in list:
    print(i)
    sq *= i
print("square is :", sq)

# display negative numbers

for i in range(-1, -40, -1):
    print(i)
# check membership in list 1
list1 = [1, 4, 8, 45, 6, 2]
list2 = [5, 1, 4, 45, 8, 5]

for i in list1:
    if i in list2:
        print("yes :", i)
    else:
        print("no :", i)

list1 = ["apple", "cat", "maggie",1, 2, 78]
list2 = ["temper", "ntr", "apple","world",2, 79]

for i in list2:
    if i in list1:
        print("yes: ", i)
    else:
        print("no: ", i)

# using break statement in for loop
counter = 0
for i in range(1, 100,):
    if i % 9 == 0:

        counter += 1
        print(i)
        if counter == 4:
           break

# using continue statement


for i in range(0, 100):
    if i % 2 == 0:
        if i % 4 == 0:
            continue
        print(i)




