'''
to display a number with a comma separator
Topics
CRUD- update
Data Type- number
State - input number
Behaviour - number with comma seperator

1. mathematical approach
step1- get the input data
step2- check the number and update with comma seperator
step3- print the output in console
'''

print("____1.builtin approach___")
x = 300000
y = 965231545
n1 = 98975646

print("input nummber x:", x)
print("after update number with comma seperator: "+"{:,}".format(x))
print("input nummber y:", y)
print("After update with comma seperator: "+"{:,}".format(y))
print("input number n1: ", n1)
print("after update nummber with comma seperator: "+"{:,}".format(n1))

n2 = 125648972255555
print("input number n2 : ", n2)
print("after update the number with comma seperator: "+"{:,}".format(n2))

m1 = 20121289656431313
print("input number: ", m1)
print("after update number with comma : "+"{:,}".format(m1))
x = "{:,}".format(m1)
print("after updating:", x)
print("___2.using algorithm approach___")
print("__3.using functions approach___")
num = 251235


def format(x):
    result = "{:,}".format(x)
    return result


print("after updating with comma:", format(num))
print("____4.using oops approach___")

class Format:
    def __init__(self, num):
        self.num = num

    def get_inputnum(self):
        print("input number:", self.num)

    def get_updatenum(self):
        print("number updated with comma:", "{:,}".format(self.num))


x = Format(789655413)
x.get_inputnum()
x.get_updatenum()