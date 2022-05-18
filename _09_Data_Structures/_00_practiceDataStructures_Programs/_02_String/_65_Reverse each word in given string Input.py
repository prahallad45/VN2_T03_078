'''
# reverse each word in a string
Topics
CRUD - update
data - string
state - input string
Behaviour - reverse the each word in a string

# mathematical approach
step1 - get the input data
step2 - check the input data and reverse the each word in a string
step3 - return the output to console

'''
print("--------1.using Builtin Approach-------")
string = "king is ruler in kingdom"
new_str = string[::-1]
print("input string:", string)
print("after reverse the string:", new_str.split())
print("--------2.using Algorithm Approach-----")
s = "king is coming"
str = ""
for i in s:
    str = i + str
print("input string:", s)
print("after reverse:", end="")
print(str.split())
print("--------3.using functions Approach-----")


def reverse():
    result = s[::-1].split()
    return result


s = "maha is one who got medal"
print("The original string  is : ", s)
print("The reversed string is : ", reverse())
print("--------4. using oops Approach---------")


class Reverse:
    def __init__(self, str1):
        self.str1 = str1

    def get_inputstring(self):
        print("input string:", self.str1)

    def get_reverse_string(self):
        print("after reverse:", self.str1[::-1].split())


s1 = Reverse("welcome to python programming language")
s1.get_inputstring()
s1.get_reverse_string()