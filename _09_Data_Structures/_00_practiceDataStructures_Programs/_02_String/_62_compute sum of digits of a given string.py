'''
# compute sum of digits of a given string

Topics
CRUD - retrieve
Type - string
State - input string
Behaviour - sum of digits of a given string

# mathematical approach
step 1: get the input data
step 2: check the input string and sum of digits of a given string
step 3: return the output
'''

print("1.using the Builtin approach")
str = "12563"
str1 = "485"
new_str = int(str)+int(str1)
print("sum of string :", new_str)

print("2.using algorithm approach")
str1 = "1254were56"
sum_digit = 0
for x in str1:
    if x.isdigit() == True:
        z = int(x)
        sum_digit = sum_digit + z

print(sum_digit)


print("3.using functions approach")


def sum_digits_string(str1):
    sum_digit = 0
    for x in str1:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z

    return sum_digit


print(sum_digits_string("123abcd45"))
print(sum_digits_string("abcd1234"))

print("4.using oops approach")


class Sum:
    def __init__(self, str1):
        self.str1 = str1

    def get_input(self):
        print("input string:", self.str1)

    def get_sumdigit(self):
        print("get sum digit:", sum_digits_string(self.str1))


s = Sum("96522mani56")
s.get_input()
s.get_sumdigit()






