'''
# to display a number in left, right and center aligned of width 10
topics
CRUD - retrieve
Type- number
state - input number
Behaviour - return the number with left,right,center aligned

# mathematical approach
step1- get the input string
step2- check the number and aligned with width 10 on left,right,center
step3- print the output in console


'''
print("--------1.using Builtin Approach-------")
x = 22
print("\nOriginal Number: ", x)
print("Left aligned (width 10)   :"+"{:< 10d}".format(x))
print("Right aligned (width 10)  :"+"{:10d}".format(x))
print("Center aligned (width 10) :"+"{:^10d}".format(x))
print("--------2.using Algorithm Approach-----")
print("number not iterable")
print("--------3.using functions Approach-----")


def format(num):
    result1 = "{:<10d}".format(num), "{:^10d}".format(num), "{:>10d}".format(num)
    return result1


num = 15
print("input number:", num)
print("after alligned width 10 on left, right, centered:", format(num))
print("--------4. using oops Approach---------")


class Allign:
    def __init__(self, num):
        self.num = num

    def get_input(self):
        print("input number:", self.num)

    def get_allignnumber(self):
        print("alligned number:", ("{:<10d}".format(self.num), "{:^10d}".format(num), "{:>10d}".format(num)))


n1 = Allign(150)
n1.get_input()
n1.get_allignnumber()