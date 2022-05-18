'''
remove spaces from a given string
Topics
CRUD - Delete
data type - string
State - input string
Behaviour - Remove spaces

# mathematical approach
step1 - get the input data
step2 - check the string for any spaces, then remove
step3 - return the string
'''

print("1.using Builtin functions")
str3 = "  manikanta good    "
string = str3.strip()
print("after removing white spaces:", string)

print("2.using Algorithm approach")
string = "    manikanta"
for var in string:
    remove = string.strip()
    print("after removing white spaces:", remove)

print("___3.using functions approach___")


def strip(str):
    result = str.strip()
    return result


x = "   john"
print("after remove whitespaces:", strip(x))

print("____4.using oops approach___")

class Strip:

    def __init__(self, str):
        self.str = str

    def get_inputstring(self):
        print("input string:", self.str)

    def get_removedstring(self):
        print("removed string:", self.str.strip())


str = Strip("   karna   ")
str.get_inputstring()
str.get_removedstring()