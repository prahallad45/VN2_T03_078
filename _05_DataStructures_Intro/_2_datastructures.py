a = {1,2,3,4,5,6,7}

# lst = [1,2,3,4,5,6,7]
# print(id(lst))
# print(id(lst[0]))
print(a)



print("------------STRING------------")
name = 'Madhu Nettem'
#0 len(name) = 5 name[len(name)-1]
print(name)
print("0th index value  : ", name[0])   # indexing
print("6th index value  : ", name[6])
print("Get partial name : ", name[0:3:2])  # slicing

office = "Oracle India Pvt Ltd"
print(office)

# List
print("------------LIST------------")

list1 = [110, 23.5, True, 'Madhu', [1,2,3], (1,['harsha']), {1:10,2:20}, {1,2,3}]
print(list1[6][1])
print("List1 : ", list1)
print("Index : ", list1[3])    # Indexing
print("Index : ", list1[3][3])    # Indexing
# print("Slice : ", list1[1:5])  # Slicing
# print(list1[7][2])



# [1,2,3,4]
# [1,2,3,4,5]
# Tuple
print("------------TUPLE------------")

tup1 = (110, 23.5, True, 'Madhu', [1,2,3], (1,2), {1:10,2:20}, {1,2,3})
print("Tuple : ", tup1)
print("Index : ", tup1[3])    # Indexing
print("Index : ", tup1[3][2])    # Indexing


print("------------DICTIONARY------------")

e_data = {'eid': 100,
          'name': 'MadhuNettem',
          'sal': 15000,
          'loc': 'Bangalore',
          'gender': 'Male',
          'eid' : 200
          }

my_emp = {'name':'harsha'}
print(my_emp['name'])


# my_emp = {['name']:'harsha'}
print(my_emp)

print("Dict data : ", e_data)
print("Dict data : ", e_data['name'])
print("Dict data : ", e_data['sal'])

# java python
print("------------SET------------")

set1 = {1, 2,2, 3, 4, 5, 6}  # unordered
print("Set1 : ", set1)

my_dc = {'A':1,'b':2}
for a in my_dc:
    print(a)
b = set({'a':1})
print("b : ", b)
print(type(b))
c = ()
print(type(c))