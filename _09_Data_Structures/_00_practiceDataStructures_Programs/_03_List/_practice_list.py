'''
list is used to store multiple items in a single variable

properties  : HDMII
1.having homogenous and heterogenous data
2.allows duplicate items
3.mutable
4.insertion order maintains
5.follows indexing mechanism
'''
# Homogenous Data

print("=========integer In LIST===========")
# 1. integers
list1 = [1, 2, 3, 8, 9]
print("integers in list1:", list1)

print("=========float In LIST===========")
# 2.float
list2 = [1.5, 2.5, 3.3, 5.2, 7.8, 8.9]
print(" float in list2 :", list2)

print("=========string In LIST===========")
# 3.string
string_list = ["joy", "far", "war","car"]
print("string in list :", string_list)

print("=========Boolean In LIST===========")
list3 =[True, False]
print("boolean in list :", list3)

print("=========lisT In LIST===========")
# 4.List in list
list4 = [[1, 2, 3], [8, 9, 5], [11, 12, 15]]
print("list in list :", list4)

print("=========Tuple In LIST===========")
list5 =[(1, 5, 3), (1,"nai", True)]
print(" tuple in list :", list5)

print("=========sets In LIST===========")
list6 = [{1, 2, 3}, {1,"mani", 5}]
print("sets in list: ", list6)

print("=========Dictionaries In LIST===========")
list7 = [{"name": "car", "eid": 256}]
print("dictionary in list :", list7)

# heterogenous data

list8 = [1, 1.5, "mai", True, [1, 8, 9], (5, 7, 2), {5, 9, 6},{"car": "audi", "year": 2016}]
print("heterogenous data : ", list8)

print("=========lisT allow duplicate valuesT===========")
list7 =[10, 10, 5, 10]
print("duplicate values in list: ", list7)

print("=========lisT maintain insertion order===========")
list1 =[1, 7, 3, 4, 8]
print("insertion order :", list1)

print("=========lisT is mutable===========")
list1 = [1, 5, 8, 16]
list1[2] = 58
print("new list: ", list1)

print("=========lisT follows indexing mechanism===========")
list = [154, 526, 789, 52]
print("indexing 2nd posiiton: ", list[2])
print("indexing oth position: ", list[0])

# sequence operation
# 1.indexing
print("=========sequence operation indexing ===========")
x = [1, 5, 8, 1.5, True, "mani", (1, 5, 9), {1, 8, 9}]
print("indexing 1st position in list: ", x[1])
print("indexing 4rth position in list: ", x[4])
print("indexing 5, 6, position :", x[5], x[6])

# 2.slicing
print("=========sequence operation sliciing ===========")
x = [1, 5, 8, 1.5, True, "mani", (1, 5, 9), {1, 8, 9}]
print("slicing from start :", x[:4])
print("slicing to end :", x[2:])
print("slicing: ", x[2:5])
print("slicing :", x[-5:-2])
# 3.adding
x = [5, 8, 9]
y = [6, 5, 6]
print("adding: ", x+y)
# 4.multiplying
x = [6, 8, 4]
z = 3
print("multiplying: ", x*z)
# 5.checking membership
r = ["mani", 1, 5, 78]
print("membership: ", 1 in r)
print("membership :", "ani" in r)
print("membership :", "mani" in r)
# 6.length of list
x = [1, 5, 8, 1.5, True, "mani", (1, 5, 9), {1, 8, 9}]
print("length of the list: ", len(x))
print("length of sub list: ", len(x[6]))

# 7.max
x = [1, 5, 8, 1.5, 70]
print("maximum data :", max(x))


# 8.min
x = [1, 5, 8, 1.5, 70]
print("minimum data: ", min(x))


# conversions
x = 10
print("convert set to integers :", float(x))
print("To string: ", str(x))
print("To boolean:", bool(x))
y = "mani kanta"
print("to tuple:", tuple(y))


# create list
thislist = ["apple", "cherry", "cane"]
print("this list :", thislist)
print(len(thislist))

'''
1.homogenous and heterogenous data
2.allow duplicate values
3.mutable
4.insertion order maintain
5.indexing mechanism'''

# homogenous
list1 = [1, 2, 34, 56]
# heterogenous
list2 = [1, 2.5, True, "mani", (5,8), {1, 2, 5}, {1: 2, "name": "mani"}, [1, 5, 8]]
#allow duplicates
list = [1, 1, 5, 101, 101]
# mutable : change the data
x = [1, 2, 50, "mani"]
x[3] = 50
print("New list :", x)
x[1] = "jam"
print("updated list :", x)
# insertion order :
y = [50, 1, 10, 3, 8]
print(y)
# indexing mechanism
f = [1, 5, True, "jani"]
print(f[1])
print("indexing 2 position: ", f[3])

print("======range or slicing ======")
g = [50, 90, 87, "karna"]
print("required slice:", f[1:4])
print("negative slicing", f[-1:-3])
print("slicing from start", f[:3])
print("slicing to end", f[2:])
#check if items
if 5 in f:
    print("True")
    if "jam"in f:
        print("true")
    else:
        print("false")
if "jam" not in f:
    print("true")

print("====change items in list======")
f[2] = "karab"
print("new list :", f)
f[1] = 1561855
print("updated list", f)

print("+++++change range of values=====")
f[1:3] = "water", "sprite"
print("updated list: ", f)
f[0:3] = 12364658, 78, "janik"
print(f)

print("+++++++insert two elements in change 2nd value========")
f[2] = 1254, 583, 479
print(f)
f[1:2] = "jhu", 158, 7896, "kiuy"
print("updated list", f)


print("===replace 2&3 with single value =====")

list2 = [1, 2, 3, 8, 96, 85]
list2[3:6] = "mani"
print(list2)
list2[3:5] = [256]
print("updated list:", list2)
thislist = ["apple", "sugar", "mango"]
thislist[1:3] = ["water"]
print("updated thislist: ", thislist)

print("====insert elements in specified position=====")

mylist =[56, 86, "kaen", 899, 78, 56]
mylist.insert(2, 896)
print("updated list :", mylist)
mylist.insert(7, "wild",)
print("updated list", mylist)
mylist.insert(8, 89)
print("updated list:", mylist)
mylist.insert(0, 100)
print(mylist)
mylist.insert(-5, "lust")
print(mylist)

print("=====APPEND=======")
# append used to add an element to end of the list

newlist = [123, 87, "jui", "kiy", 789, 449]
newlist.append(9654)
newlist.append("mabjbbbsv")
print("updated list:", newlist)

print("====INSERT elements======")
newlist.insert(2, "miss")
print(newlist)
newlist[2] = "mani", "kanta"
print(newlist)

print("====EXTEND =====")
newlist1 = ["rrr", "rise", "roar", "revolt"]
newlist.extend(newlist1)
print(newlist)
newlist1.extend(newlist)
print(newlist1)

print("====ADD ANY ITERABLE=====")
newlist.extend(f)
print("extended newlist : ", newlist)

print("====REMOVE=====")
# remove used to remove the item
fire = ["stick", "raw", "cover", "hand"]
fire.remove("raw")
print(fire)


print("=========using POP========")
# pop used to remove specified index or pop() goes to end
fire.pop(1)
print(fire)
# remove 5th position item
list2.pop(5)
print(list2)
# removes an end element
list2.pop()
print(list2)
# removes an 0th element
list2.pop(0)
print(list2)

print("======using DEl=======")

del newlist[0]
print(newlist)
del newlist[5]
print(newlist)
del newlist
# deletes entire newlist

print("=====using CLEAR() ======")
v = [1, 2, 3, 8, 96, 78]
v.clear()
print(v)
f = [256, 896, 789, "kany"]
y = ["mani", "juab", "ser"]
f.append(8)
print(f)
f.extend(y)
print(f)
f.insert(5, "mani")
print(f)
f.remove("mani")
print(f)
f.pop()
print(f)
f.pop(5)
print(f)
del f[5]
print(f)
del f[1]
print(f)
f.clear()
print(f)

print("======= Loops through list=============")
print(newlist1)
for x in newlist1:
    print("items in list :", x)

print("====using while loop====")
i = 0
while i < len(newlist1):
    print("items :", i)
    print(newlist1[i])
    i += 1
[print(x) for x in newlist1]

list = [1, 8, "mani", "wat"]
for x in list:
    print("items :", x)

[print(x) for x in list]

i = 0
while i < len(list):
    print(list[i])
    print("items in list :", i)
    i += 1

print("====List Comprehension=======")
list1 = ["mani", "mustafa", "karna", "fan", "Duck"]
new = []
for x in list1:
    if "n" in x:
        new.append(x)
    print(new)


print("====sort======")
list1.sort()
print("after alphabetically sorting", list1)
t = [50, 78, 788, 100, 10]
t.sort()
print("after numerically sorted:", t)

print("======reverse sorting=======")
list1.sort(reverse=True)
print(list1)
t.sort(reverse=True)
print("after reverse sorting", t)

def myfunc(n):
    return abs(n - 20)
list = [5, 8, 10, 2, 20, 87]
list.sort(key = myfunc)
print(list)


print("=====copy =====")
mylist = list.copy()
print(mylist)
newlist = mylist.copy()
print(newlist)




print("+++++++join+++++++")
list1 = [1, 2, 8, 15, 63, 78]
list2 = ["mani", "can"]
list3 = list1 + list2
print(list3)

list4 = list1.append("mani")
print(list4)


list1 = [1, 6, 4, 8, 9, 10]
list2 = [78, 96, 15]

# list functions
'''
1.indexing
2.slicing
3.adding
4.multipliying
5.checking membership
6.min
7.max
8.len
'''
print(list1[1])
print(list2[2])
print(list2[0])

print("slicing:", list2[0:])
print("slicing: ", list1[:4])

#adding
print("adding two list:,", list1+list2)
print("adding:", list2+list2)

# multiplying

print("multiplying:", list1*2)
print("multipling:", list1)



