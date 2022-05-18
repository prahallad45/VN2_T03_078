
# Using for loop

list = [10,3,22,5,32,54]
for i in list:
    print(i)

# Using while loop
list2 = [12,54,64,122,3]
length = len(list2)

i = 0
while i < length:
    print(list[i])
    i += 1

#display only even num
list3=[1,4,2,6,5,33,76,11]
print("even nos are:")
for i in list3:
    if i%2==0:
        print(i)

#To display elements by index wise(-Ve, +ve)
list4=[44,35,72,80,90,12]
print('display elements by index wise')
print(list4[3])
print(list4[2])