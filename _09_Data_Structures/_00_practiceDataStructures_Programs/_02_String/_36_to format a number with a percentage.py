'''
# to format a number with a percentage
Topics
CRUD - update
Type - number
State - input number
Behaviour - update with %

1.mathematical approach
step1- get input data
step2- check the number and update with %
step 3- print the uutput in console

'''
print("___1.using Builtin method____")
x = 70932684
print("input number:", x)
print("after updating number with %:"+"{:%}".format(x))
print("___2.using algorithm approach____")
print("___3.using functions approach___")


def update(x):
    result = "{:%}".format(x)
    return result


num = 986464
print("after updating number with %:", update(num))
print("____4.using oops approach___")
class Update:
    def __init__(self, num):
        self.num = num

    def get_inputnumber(self):
        print("input number:", self.num)

    def get_updatenumber(self):
        print("updated number:", "{:%}".format(self.num))


n1 = Update(6281651717)
n1.get_inputnumber()
n1.get_updatenumber()