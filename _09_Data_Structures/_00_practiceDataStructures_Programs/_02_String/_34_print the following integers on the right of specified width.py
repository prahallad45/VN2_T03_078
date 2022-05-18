'''
# print the following integers with '*' on the right of specified width

Topics
CRUD - Retrieve
data type- number
State - numbers
Behavior - print integer numbers with  zero on right

# 1.mathematical approach
step1 = get the input
step2 = check input numbers having zeros on right
step3 = print the values in console
'''
print("--------1.using Builtin Approach-------")
x = 300
y = 123
print("\nOriginal Number: ", x)
print("Formatted Number(right padding, width 2): "+"{:*< 3d}".format(x))
print("Original Number: ", y)
print("Formatted Number(right padding, width 6): "+"{:*< 7d}".format(y))
print("--------2.using Algorithm Approach-----")
print("number not iterate in algorithm approach")
print("--------3.using functions Approach-----")


def format(num):
    result = "{:*<4d}".format(num)
    return result
num = 12
print("input number:", num)
print("After formatting with specified width:", format(num))
print("--------4. using oops Approach---------")


class Format:
    def __init__(self, num):
        self.num = num

    def get_input(self):
        print("input number:", self.num)

    def get_formatnum(self):
        print("after formatting with specified width:", "{:*<5d}".format(self.num))


n1 = Format(1)
n1.get_input()
n1.get_formatnum()