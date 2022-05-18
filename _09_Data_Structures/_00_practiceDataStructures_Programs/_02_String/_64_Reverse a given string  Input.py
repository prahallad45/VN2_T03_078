'''
# Reverse a given string  Input : "Python"   Output : "nohtyP"
Topics
CRUD - update
data - string
state - input string
Behaviour - reverse the words in a string

# mathematical approach
step1 - get the input data
step2 - check the input data and reverse the words in a string
step3 - return the output to console

'''
print("--------1.using Builtin Approach-------")
string = "king is ruler in kingdom"
new_str = string.split()
print("input string:", string)
print("after reverse the string:", new_str[::-1])
print("--------2.using Algorithm Approach-----")
s = "king is coming"
str = ""
for word in s:
    word.split()
    s1 = s.split()
print("input string:", s)
print("after reverse:", s1[::-1])
print("--------3.using functions Approach-----")


def reverse(s):
    split = s.split()
    result = split[::-1]
    return result


s = "maha is one who got medal"
print("The original string  is : ", s)
print("The reversed string is : ", reverse(s))
print("--------4. using oops Approach---------")


class Reverse:
    def __init__(self, str1):
        self.str1 = str1

    def get_inputstring(self):
        print("input string:", self.str1)

    def get_reverse_string(self):
        print("after reverse:", reverse(self.str1))


s1 = Reverse("welcome to python programming language")
s1.get_inputstring()
s1.get_reverse_string()