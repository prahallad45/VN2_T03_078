'''
# 4 Copies of last 2 chars
Topics
CRUD - create
Type - String
state - input string
Behaviour - insert string

# mathematical approach
step1- get the input data
step2- check the input string and make copy of last 2 chars
step3- return the output in console

'''
print("1.using Builtin Approach")
string = "manikanta"
new_str = string[-2:]*4
print("input string:", string)
print("copies of last 2 chars in string:", new_str)
print("2.using Algorithm Approach")
str2 = "johnny"
for i in str2:
    str2 = str2[-2:]*4

print("after create 4 copy:", str2)
print("3.using functions Approach")


def copy():
    result = str2[-2:]*4
    return result


print("input string:", str2)
print("after create 4 copy:", copy())
print("4. using oops Approach")


class Copy:
    def __init__(self, string1):
        self.string1 = string1

    def get_input_string(self):
        print("input string:", self.string1)

    def get_copy_string(self):
        print("after create 4 copy of string:", self.string1[-2:]*4)


m = Copy("programming")
m.get_input_string()
m.get_copy_string()