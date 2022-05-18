total = 1
list1 =[int (x) for x in input("Enter element seperated by space:").split( )]
for x in range(0, len(list1)):
    total = total * list1[x]

print("mul of all elements : ", total)
