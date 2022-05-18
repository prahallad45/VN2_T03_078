
# Dictionary is mutable

# CREATE
data = {1: 'One', 2: 'Two', 3: 'Three', 'id': '100'}

# RETRIEVE
print("Dictionary : ", data, type(data))
print("Dict item  :", data[2])
print("Dict item  :", data['id'])

# UPDATE
data[2] = 'Twenty'
data['id'] = 200
print("Dictionary update: ", data)

# DELETE
del data[3]
del data['id']
print("Dictionary delete: ", data)

data.clear()
print("Dictionary delete: ", data)

x = 10
print("X : ", x)
del x
# print("X : ",x)

del data
# print("Dictionary delete: ", data)


# create a dictionary contianing name id as keys 
# you need to ask user for the input to assign values to name and id
# but you need to store all names and ids

"""
inp = {'name': 'harsha', 'id': 123}
5
input(enter how many times you need to enter values)
while 
print(enter you name:)
print(enter your id)    

[{'name': 'harsha', 'id': 123},{'name': 'rajith', 'id': 456},{'name': 'ram', 'id': 759}]
"""





