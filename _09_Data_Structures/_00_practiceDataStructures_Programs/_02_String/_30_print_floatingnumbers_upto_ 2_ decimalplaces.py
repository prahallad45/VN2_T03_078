'''

To print the following floating numbers upto 2 decimal places
Topics
CRUD - Retreive
data type- number
State - nummbers
Behavior - print float nummbers

# 1.mathematical approach
step1 = get the input
step2 = check input having float numbers upto 2 decimals
step3 = print the values in console

'''
print("____2.using Builtin approach____")
num = 2.154327
format_float = "{:.2f}".format(num)
print("print float numbers upto 2 decimals:", format_float)

import math
float = 152.15648
print("The value of number is:", end="")
print(math.trunc(float))

float = 12.16758
print("the smallest integer:", end="")
print(math.ceil(float))

float = 12.16785
print("The greatest integer smaller than number is:", end="")
print(math.floor(float))

number = 1.345
f = '{0:.3g}'.format(number)
print("number with two decimals:", f)
print("after the number rounded:", round(number))

limit_float = round(number, 2)
print("after the float number rounded:", limit_float)

print("____3.using functions approach___")


def float(x):
    result = "{:.2f}".format(x)
    return result


num = 5.3645
print("after update the number:", float(num))

print("___4.using oops approach____")


class Float:
    def __init__(self, num):
        self.num = num

    def get_inputnumber(self):
        print("input number:", self.num)

    def get_updatenum(self):
        print("update number with 2 decimals:", "{:.2f}".format(self.num))


n1 = Float(2356487)
n1.get_inputnumber()
n1.get_updatenum()









