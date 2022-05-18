'''
# remove existing indentation from all of the lines in a given text
Topics
CRUD - delete
Type - String
state - input string
Behaviour - remove existing indentation

# mathematical approach
step1- get the input data
step2- check the input string and remove existing indentation
step3- return the output in console
'''
print("--------1.using Builtin Approach-------")
string = "     manikanta"
print("input string:", string)
print("after remove indentation:", string.strip())
print("--------2.using Algorithm Approach-----")
for i in string:
    result = string.strip()
print("after removing:", result)
print("--------3.using functions Approach-----")


def remove():
    result = string.strip()
    return result


print("after removing:", remove())
print("--------4. using oops Approach---------")


class Remove:
    def __init__(self, string):
        self.string = string

    def get_input_string(self):
        print("input string:", self.string)

    def get_removed_string(self):
        print("after removing indentation:", self.string.strip())


s1 = Remove("    vnsquare")
s1.get_input_string()
s1.get_removed_string()