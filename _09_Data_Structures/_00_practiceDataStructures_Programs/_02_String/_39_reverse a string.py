'''
# reverse string
Topics
CRUD - update
data - string
state - input string
Behaviour - reverse the string

# mathematical approach
step1 - get the input data
step2 - check the input data and reverse string
step3 - return the output to console

'''
print("--------1.using Builtin Approach-------")
string = "manikanta"
new_str = string[::-1]
print("after reverse the string:", new_str)
print("--------2.using Algorithm Approach-----")
s = "manikanta"
str = ""
for i in s:
    str = i + str
print("after reverse:", end="")
print(str)
print("--------3.using functions Approach-----")


def reverse():
    result = s[::-1]
    return result


s = "vn square"
print("The original string  is : ", s)
print("The reversed string is : ", reverse())
print("--------4. using oops Approach---------")


class Reverse:
    def __init__(self, str1):
        self.str1 = str1

    def get_inputstring(self):
        print("input string:", self.str1)

    def get_reverse_string(self):
        print("after reverse:", self.str1[::-1])


s1 = Reverse("welcome")
s1.get_inputstring()
s1.get_reverse_string()