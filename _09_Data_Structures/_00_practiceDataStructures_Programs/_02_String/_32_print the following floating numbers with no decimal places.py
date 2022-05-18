'''
# print the following floating numbers with no decimal places
Topics
CRUD - Retrieve
data type- number
State - numbers
Behavior - print float numbers

# 1.mathematical approach
step1 = get the input
step2 = check input numbers having float numbers no decimals
step3 = print the values in console

'''
print("--------1.using Builtin Approach-------")
float = 125.153
print("input number", float)
print("after removing decimals:", int(float))
print("--------2.using Algorithm Approach-----")
print("number is not iterable in algorithm approach")
print("--------3.using functions Approach-----")
number = 13.345


def round():
    result = "{0:.2g}".format(number)
    return result


print("input number:", number)
print("after removing decimals:", round())
print("--------4. using oops Approach---------")

class Round:
    def __init__(self, num):
        self.num = num

    def get_input(self):
        print("input num:", self.num)

    def get_remove_decimal(self):
        print("after removing decimals:", "{0:.2g}".format(self.num))


n1 = Round(12.3658)
n1.get_input()
n1.get_remove_decimal()