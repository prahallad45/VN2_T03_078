#union -all uniques values
a = {1,2,3,4}
b = {3,4,5,6}

print( a.union(b))

#intersertion -return only common 
a = {1,2,3}
b = {3,4,5}

print( a.intersection(b))

#difference -return non common values of 1st set
a = {1,2,3}
b = {3,4,5}

print( a.difference(b))

#symmetric difference -return non common values of both set
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
print(A.symmetric_difference(B))



