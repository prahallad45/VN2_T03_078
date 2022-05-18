#add()
s= {'p','g','k','d','f'}
s.add('s')
print(s)
#update
A = {'a', 'b'}
B = {1, 2, 3}
result = A.update(B)
print(A)

#copy() shallow copy
set1 = {1, 2, 3, 4} 
set2 = set1.copy() 
print(set2)

#pop 
col= {'red','orange','blue'}
col.pop()
print(col)

#remove
#discard is similar with remove but method will raise an error 
# if the specified item does not exist, and the discard() method will not.
s = {'pg','a','do','as','if'}
s.remove('do')
print(s)
s.discard('as')
print(s)

#clear()
s.clear()
print(s)

