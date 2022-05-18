'''
#  Length of first 3 chars
Topics
CRUD - retrieve
Type - String
state - input string
Behaviour - count of first 3 chars in string

# mathematical approach
step1- get the input data
step2- check the input string and count of first 3 chars
step3- return the output in console
'''
print("--------1.using Builtin Approach-------")
str1 = "manikanth"
new_str = len(str1[:3])
print("input string:", str1)
print("count of first 3 chars:", new_str)
print("--------2.using Algorithm Approach-----")
str2 = "johnny johnny"
for i in str2:
    string = len(str2[:3])
print("input string:", str2)
print("count of first 3 chars:", string)
print("--------3.using functions Approach-----")
string = "vn square"


def count():
    result = len(string[:3])
    return result


print("input string:", string)
print("count f first 3 chars:", count())
print("--------4. using oops Approach---------")


class Count:
    def __init__(self, string2):
        self.string2 = string2

    def get_input_string(self):
        print("input string:", self.string2)

    def get_count_string(self):
        print("count of 3 chars:", len(self.string2[:3]))


s = Count("manikanta")
s.get_input_string()
s.get_count_string()
