'''
# sum of elements in list

Topics
CRUD Retrieve
DATA number
state input list with numbers
Behaviour: sum of elements in list

# mathematical function
step 1: get input data
step 2: check elements in list and sum of it
step 3: print output
'''
print("___1.using builtin approach_____")
list1 = [1, 2, 3, 5]
new_list = sum(list1)
print(new_list)

print("____2.using algorithm approach__-")

# Python program to find sum of elements in list

total = 0
# creating a list
list1 = [11, 5, 17, 18, 23]

# Iterate each element in list

for ele in range(0, len(list1)):
    total = total + list1[ele]

print("Sum of all elements in given list: ", total)

print("____3.using functions____")


from functools import reduce

result = reduce(lambda x, y: x + y, list1)
print("sum of elements in list1:", list1)

print("___4.using oops approach__")


class Sum:
    def __init__(self, list1):
        self.list1 = list1

    def get_inputlist(self):
        print("input list:", self.list1)

    def get_sumlist(self):
        print("sum list:", sum(self.list1))


l1 = Sum([1, 5, 15])
l1.get_inputlist()
l1.get_sumlist()