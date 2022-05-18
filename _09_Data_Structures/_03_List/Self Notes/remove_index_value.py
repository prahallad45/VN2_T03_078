# normal 
lst=[10,20,40,44,66,22]
lst.pop(2)
print(lst)

#using function
def remove1(lst):
    lst.pop(2) #here 2nd index value is removed
    return lst

lst=[22,34,56,66,23]
print(remove1(lst))