# set
'''
1. immuatable and not allow duplicate values
2.allow homogenous and heterogenous data
3.unoreded  (using hashing mechanism)
4.allow indexing and slicing mechaanism

set methods
1.add  set.add(1)
2.update set1.update(set2)
3.remove set1.remove(96) it will shown error again using same element
4.discard set.discard(15) it will not give error by using saame element
5.pop() set1.pop() it will remove any element it is unordered we don"t know
6. clear() set5.clear() the set  returns empty set
7. del () del set5 delete the set

join sets
1. union
2. intersection
3.symmetric difference


'''

set1 = {1, 2, 3, 4, 5, 10}
# set[1] = 50 shown error set is immutable does not change data in it

print("homogenous data:", set1)
set2 = {"abc", 34, True, 40, "male"}
print("heterogenous data:", set2)
set3 = {1, 1, 5, 5, 10}
print("not allowed duplicates:", set3)
set4 = {1, 15, 200, 50, 10, "a", "d", "s"}
print("unordered using hashing mechanism:", set4)

# length = len(set1)

print("length of set1:", len(set1))
print("length of set2:", len(set2))
print("length of set3:", len(set3))
print("length of set4:", len(set4))

# access items

for x in set1:
    print("data in set1:", x)

if 10 in set1:
    print("yes")

# add

set1.add("orange")
print("after adding:", set1)

set1.add("water")
print("after adding:", set1)

# update
set1.update(set3)
print("after updating :", set1)

# Remove # it will shown error using removed element after remove an element

set5 = {156, 200, 96, 5, 4, 32, 15}
set5.remove(5)
print("after removing:", set5)
set5.remove(156)
print("after removing:", set5)

# discard  # it will not shown error while using the discard element for same function

set5.discard(32)
print("after discarding:", set5)
set5.discard(32)

# pop removes end element of set  (sets are unordered so we don't know which element to be removed)

x = set5.pop()
print("after pop:", x)
print("after pop", set5)

# clear()

set1.clear()
print("after clearing:", set1)

# del(set1)
del set5

# union()

set1 = {15, 1, 2, 3, 4, 5}
set2 = {1, 5, 6, 9, 10}
set3 = set1.union(set2)
print("after union:", set3)

set1 = {15, 1, 2, 3, 4, 5}
set2 = {1, 5, 6, 9, 10}
set1.update(set2)
print("after updating :", set1)

# intersection returns only elements available in both sets

set1 = {15, 1, 2, 3, 4, 5}
set2 = {1, 5, 6, 9, 10}
set3 = set1.intersection(set2)
print("after intersection:", set3)

set = set()
set1 = {15, 1, 2, 3, 4, 5}
set2 = {1, 5, 6, 9, 10}
set1.intersection_update(set2)
print("intersection update: ", set1)

# symmetric_difference_update keep set with all elements which are in both sets not same elements

set1 = {15, 1, 2, 3, 4, 5}
set2 = {1, 5, 6, 9, 10}
set1.symmetric_difference_update(set2)
print("after symmetric difference update:", set1)

# symmetric difference returns new set with all elements expect same elements in both
set1 = {15, 1, 2, 3, 4, 5}
set2 = {1, 5, 6, 9, 10}
set3 = set1.symmetric_difference(set2)
print("after symmetric difference:", set3)




'''
# differences 
s.no     List                        Tuple                         Dictionaries                 set

1.  allow homogenous and         allow homogenous and          having key value pairs      allow homogenous and
    Heterogenous elements        Heterogenous elements                                     Heterogenous elements

2.  allow duplicates             allow duplicates              not allow duplicates        not allow duplicates

3.  mutable                      immutable                   dictionaries  are mutable     immutable
                                                            keys ere immutable and unique
                                                            
4. ordered allow insertion order   allowed                    not allowed using hashing mechanism 

5. indexing mechanism                                         not allowed 
'''



















