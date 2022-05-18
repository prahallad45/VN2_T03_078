'''
# reverses a string if it's length is a multiple of 4
Topics
CRUD - update
Type - String
state - input string
Behaviour - reverse string if length multiple of 4

# mathematical approach
step1- get the input data
step2- check the input string and reverse string
step3- return the output in console
'''
print("--------1.using Builtin Approach-------")
string = "williamson"
print("--------2.using Algorithm Approach-----")
str1 = "warneris"
if len(str1) % 4 == 0:
    print("reversed string:", ''.join(reversed(str1)))
print("--------3.using functions Approach-----")


def reverse_string(str1):
    if len(str1) % 4 == 0:
        result = ''.join(reversed(str1))
        return result


print(reverse_string('abcd'))
print(reverse_string('python'))
print("--------4. using oops Approach---------")


class Reverse:
    def __init__(self, str3):
        self.str3 = str3

    def get_input_string(self):
        print("input string:", self.str3)

    def get_reverse_string(self):
        print("reverse string:", reverse_string(self.str3))


str = Reverse("manikant")
str1 = Reverse("manikanta")
str.get_input_string()
str.get_reverse_string()
str1.get_input_string()
str1.get_reverse_string()
