print("======Join two list====")
list1 = [1, 58, 96]
f = ["a", "c"]
list3 = list1 + f
print(list3)


# append
l1 = [156, "mani", 86, 97]
l2 = ["y", "try"]
for x in l2:
    l1.append(x)
    print(l1)

l2.extend(list1)
print(l2)


# append
ki = [125]
le = ["mani", "wild", "car"]
for x in ki:
    le.append(ki)
print(le)

le.append(12)
print(le)

# clear
le.clear()
print(le)

list1 = [1, 2, 3, 5, 7, 1, 78, 1]
list2 = list1.copy()
print(list2)

# count
x = list1.count(1)
print(x)
print("===append==")
x = [1, 2, 10]
y = []
y.append(x)
print(y)
x.append("orange")
print(x)
x.append(5)

# list functions

# append, insert, extend   - update
# pop, remove              - Delete
# index                    - Retrieve
# count                    - Retrieve
# copy                     - create
# sort                     - update
# reverse                  - update

# Create operation in list

# copy - return the copy of a list

print("=========copy()======")
list1 = [1, 2, "mani"]
list2 = list1.copy()
print("After copying new list:", list2)

x = [1, 5, "k", True, "welcome"]
y = x.copy()
print("After copying :", y)


# retrieve operation = count(), index()

# count () = returns the number of repeated elements occur in list
x = [1, 1, 5, "a", 1, 5, 8, "a"]
print("number of 1 elements in list x:", x.count(1))
print("number of a elements in list x", x.count("a"))
print("number of 8 elements in list x", x.count(8))

list = ["mani", "kanta", "parle", "mani"]
x = list.count("mani")
print("number of repeated elements:", x)

# index():returns the specified value lowest index appears
print("========index()=====")
x = [1, 1, 5, "a", 1, 5, 8, "a"]
print("position of a", x.index("a"))
print("index of 8 in list", x.index(8))

list = ["mani", "kanta", "parle", "mani"]
print("index of parle in list", list.index("parle"))
print("index of kanta in list", list.index("kanta"))

# update =append(), insert(), extend(), reverse(), sort()

# append() = add elements to the end of list appends only end of the list
print("====append====")
list1 = [1,85, 96, 102, 78, "p", 56, "q"]
list2 = [986, 456, 786]
list1.append(1)
list1.append(list2)
list1.append(True)
list1.append("sre")
list1.append(568785)
list1.append(5)
list1.append(("mani","kanta"))
list1.append({156, 7895, "mani"})
list1.append({1: 45, "id": 154})

print("after appends the list", list1)

# extends = extend the sequence
list2 = [986, 456, 786]
list2.append(("hello", "world"))
print("After appends", list2)
list2.extend(("hello", "world"))
print("After extend", list2)
list2.append(1)
list2.extend((1, 5, 856))
print("after extend", list2)

# insert = insert elements in specified index

list2 = [986, 456, 786]
list2.insert(2, 50)
print("after inserting", list2)
list2.insert(0, "hello")
print("after inserting", list2)
list2.insert(1, 6444+444)
print("after inserting", list2)
list2.insert(3, "welcome to the word")
print("after inserting", list2)

# reverse = reverse the list
list2.reverse()
print("after reverse the elements", list2)
list1 = [1, 56, 78, 45, 96, "hello", "main", "function"]
list1.reverse()
print("after reverse the list", list1)

# sort = return the list in an increasing order,alphabetically
list1 = [1, 56, 78, 45, 96,]
list1.sort()
print("after sorting", list1)
list2 = ["hello", "main", "function", "b", "c", "k", "j"]
list2.sort()
print("after sorting", list2)

# reverse sorting

list1.sort(reverse=True)
print("after reverse sorting", list1)
list2.sort(reverse=True)
print("after reverse sorting", list2)

# delete = pop()- removes index position or end index, remove - remove throgh value
list2 = ["hello", "main", "function", "b", "c", "k", "j"]
list2.pop()
print("after pop the list2 :", list2)
list2.pop(5)
print("after pop the 5 th index in list2 :", list2)
list2.remove("main")
print("after remove :", list2)
list2.remove("c")
print(list2)




'''
update
1.append() = list.append((1,2,3,"mani"))
2.insert() = list.insert(2, 50) or list[2] = 50
3.extend() = list.extend((1,2,3))
4.reverse = list.reverse()
5.sort()  = list.sort() or list.sort(reverse=True)

retrieve
6.count() = list.count("mani") or list.count(1)
7.index() = list.index("mani) returns index position

delete
8.pop() = list.pop() or list.pop(1) deletes value through index
9.remove = list.remove("mani") deletes value throngh value

create
10. copy() = list.copy()



'''
















# delete = pop(), remove()









