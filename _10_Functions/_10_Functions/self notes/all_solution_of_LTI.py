#reverse the string

def rev(str1):
    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(rev('prahallad'))


#----------XXXX-----------
#many list item to single integer
L = [11, 33, 50]
print("Original List: ",L)
x = int("".join(map(str, L)))
print("Single Integer: ",x)

#-----------X-------------------
#replace the nth place value to n-1
from itertools import zip_longest, chain, tee
def replace2copy(lst):
    lst1, lst2 = tee(iter(lst), 2)
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))
n = [0,1,2,3,4,5]
print(replace2copy(n))

#------------------xx--------------------


def printValues():
	l = list()
	for i in range(1,31):
		l.append(i**2)
	print(l[5:])
printValues()
names = ['Chris', 'Jack', 'John', 'Daman']
print(names[-1][-1])
