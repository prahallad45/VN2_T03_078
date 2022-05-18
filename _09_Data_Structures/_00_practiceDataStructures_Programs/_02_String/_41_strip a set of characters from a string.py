'''
# strip a set of characters in a string
Topics
CRUD - delete
data - string
state - input string
Behaviour - strip a set of special characters in a string

# mathematical approach
step1 - get the input data
step2 - check the input data and strip special chaaracters in a string
step3 - return the output to console

'''
print("--------1.using Builtin Approach-------")
string = "@##king is ruler in kingdom @#$%"
import re
print(re.sub('[^A-Za-z0-9]+', '', string))
print("--------2.using Algorithm Approach-----")
string = "Special $#! characters   spaces 888323"
for i in string:
    output = re.sub('[^A-Za-z0-9]+', '', string)
print("input string:", string)
print("After strip of characters:", output)
print("--------3.using functions Approach-----")
string = "@@%& kingdom"


def func():
    result = re.sub('[^A-Za-z0-9]+', '', string)
    return result


print("input string:", string)
print("After strip of characters:", func())
print("--------4. using oops Approach---------")


class Strip:
    def __init__(self, str1):
        self.str1 = str1

    def get_inputstring(self):
        print("input string:", self.str1)

    def get_stripstring(self):
        print("after strip:", re.sub('[^A-Za-z0-9]+', '', self.str1))


s1 = Strip("!!@@# welcome to python programming @##language")
s1.get_inputstring()
s1.get_stripstring()