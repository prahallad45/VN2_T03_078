#deep copy
l=['ram','ravan','sita','virat']
l1=[]
l1=l
l1.append('rajesh')
print(l,id(l))
print(l1,id(l1))

#shallow copy

l3=[1,4,6,8,9,33]
l4=[]
l4=l3.copy()
l3.append(100)
print(l3,id(l3))
print(l4,id(l4))