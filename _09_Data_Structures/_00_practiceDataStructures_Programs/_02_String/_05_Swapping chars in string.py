'''
# Swapping chars in string
Topics
CRUD - update
data type - string
state - input string
Behaviour - swap the characters

# mathematical approach
step1 - get the input string
step2 - check the input and swap the chars
step3 - return the output

'''
print("1.using Builtin approach")
str = "javed KHAN"
new_str = str.swapcase()
print("input string:", str)
print("After Swapping :", new_str)
print("2.using Algorithm approach")
string = "KrishNa"
for var in str:
    print("input string:", string)
    print("after swapping:", string.swapcase())
print("3.using Functions approach")


def swapcase():
    result = str.swapcase()
    return result


str = "RAma krishNa"
print("input string:", str)
print("After Swapcase:", swapcase())
print("4.using oops approach")


class Swap:
    def __init__(self, str1):
        self.str1 = str1

    def get_inputstring(self):
        print("input string:", self.str1)

    def get_swapcasestring(self):
        print("swapcasestring:", self.str1.swapcase())


s1 = Swap("RAMa rama Krishna")
s1.get_inputstring()
s1.get_swapcasestring()