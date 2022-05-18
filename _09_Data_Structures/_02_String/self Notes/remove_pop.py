lst=[1,2,3,1,4]
lst.remove(1) #remove the 1st occurance in the list
print(lst)
lst.pop()  #remove the last element of the list
print(lst) 
lst.pop(1) #it remove the particular index value
print(lst)

lst.clear() #it remove all the element
print(lst)


#to remove the duplicate in the list 
list2=[22,55,64,2,5,2,6,5,7]
a=list(set(list2)) 
print(a)

del list2[:]
print(list2)


#------------------
list4=["pg","sfs","raja","raj","pg"]
for x,y in enumerate(list4):
    print(x,y)

#--------------
#concatenate two lists by +
a=[22,44,65]
b=[10,20,30]
print(a+b)

#------------------



