'''
# to add a prefix text to all of the lines in a string
Topics
CRUD - update
Type - String
state - input string
Behaviour - add prefix

# mathematical approach
step1- get the input data
step2- check the input string and remove existing indentation
step3- return the output in console

'''
print("--------1.using Builtin Approach-------")
string = "manikanta"
new_string = "i am "+string
print("input string:", string)
print("after adding prefix:", new_string)
print("--------2.using Algorithm Approach-----")
for i in string:
    output = "welcome "+string
print("After adding:", output)
print("--------3.using functions Approach-----")


def add_prefix():
    result = prefix + string
    return result


prefix = "hi "
print("after adding :", add_prefix())
print("--------4. using oops Approach---------")


class Prefix:
    def __init__(self, string):
        self.string = string

    def get_input(self):
        print("input string:", self.string)

    def get_addprefix(self):
        print("After adding :", prefix + self.string)


s = Prefix("women")
prefix = "super "
s.get_input()
s.get_addprefix()