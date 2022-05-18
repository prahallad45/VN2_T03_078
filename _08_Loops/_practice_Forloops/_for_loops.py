# using for loop display strings

text = "welcome"
for var in text:
    print("Elements", var)
print("------------------------")

sbi = " your balance is 25 "
for var in sbi:
    print("Elements : ", var)

print("-------------------------")

# using loops diplay list integer,float,string
# using loops diplay tuples
# using loops diplay sets
# using loops diplay dictionaries keys,values

x = {'fruit': 'banana', 'car': 'audi', 'bike': 'fz'}
for c in x:
    print("keys :", c)

for c in x.keys():
    print("keys :", c)

for c in x.values():
    print("values :", c)

# using for loop in sets:

set1 = {1, 2, 3, 8, 9}
for values in set1:
    print("elements :", values)

set2 = {1.85, 7.2352, 89.1545, 78.2326}
for floats in set2:
    print("values :", floats)

set3 = {"car", "hello world", "narappa"}
for strings in set3:
    print("strings :", strings)

# using for loop in strings
x = "hello world"
for elements in x:
    print("strings :", elements)

# using for loop in tuples

tup1 = (1, 2, 3, 99, 126, 896, 785)
tup2 = (1.5, 7.264, 6.35, 789.32)
tup3 = ("blast", "buster", "cinema")
for elements in tup1:
    print("tuple values :", elements)
for elements in tup2:
    print("tuple values :", elements)
for elements in tup3:
    print("tuple values :", elements)

# using for loop in list

list1 = [156, 2031, 7896, 12555]
list2 = [15.23, 78.26, 786.23]
list3 = ["narappa", "seenappa", "muniappa"]
for values in list1, list2, list3:
    print("elements :", values)

for values in list1:
    print("elements :", values)
for values in list2:
    print("elements :", values)
for values in list3:
    print("elements :", values)















