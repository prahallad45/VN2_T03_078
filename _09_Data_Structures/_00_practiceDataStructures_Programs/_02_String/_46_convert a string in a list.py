'''

convert a string in a list

'''
'''
convert string into list

Topics
CRUD - update
data - string
state - input string
Behaviour - convert string into list

# mathematical approach
step1 - get the input data
step2 - check the input data and convert string into list
step3 - return the output to console

'''
print("--------1.using Builtin Approach-------")
string = "infinite"
str = list(string.split())
print("after converting:", str)

print("--------2.using Algorithm Approach-----")
string = "characters"
for i in string:
    output = list(string.split())
print("input string:", string)
print("After converting:", output)
print("--------3.using functions Approach-----")
string = "kingdom"
st1 = "python programming language"


def convert(x):
    li = list(x.split(" "))
    return li


print("input string:", string)
print("After converting:", convert(string))
print("input string:", st1)
print("after converting:", convert(st1))
print(list(st1))
print("--------4. using oops Approach---------")


class List:
    def __init__(self, str1):
        self.str1 = str1

    def get_inputstring(self):
        print("input string:", self.str1)

    def get_list(self):
        print("After converting:", list(self.str1.split()))


s1 = List("welcome to python")
s1.get_inputstring()
s1.get_list()