'''
# print even and odd numbers

Topics
CRUD - RETREIVE
Data Type - number
state - input number
behaviour - input number

'''
print("---using algorithm approach---")
count = 0
for i in range(5):
    count += 1
    if i % 2 == 0:
        print("even numbers are:", i)
    else:
        print("odd numbers are:", i)
    i += 1
print("____using functions approach____")


def evennumbers(x):
    for i in range(x):
        if i % 2 == 0:
            print("even numbers", i)
        else:
            print("print odd numbers:", i)

        i += 1

    result = i
    return result


print("even and odd numbers:", evennumbers(5))


list1 = [1, 2, 3, 4, 5, 100]


def even():
    result = list(filter(lambda x: (x % 2 == 0), list1))
    return result


print(even())











