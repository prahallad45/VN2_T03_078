'''
# program to sort a string lexicographically
Topics
CRUD - update
Type - String
state - input string
Behaviour - sort string lexicographically

# mathematical approach
step1- get the input data
step2- check the input string and sort by lexicographically
step3- return the output in console
'''
print("--------1.using Builtin Approach-------")
str1 = "open your mouth haha"
str2 = str1.split()
str2.sort()
print("after sorting:", str2)
print("--------2.using Algorithm Approach-----")
string = "welcome to python programming language"
for i in string:
    result = string.split()
    result.sort()
for i in result:
    print("after sorting:", i)

print("--------3.using functions Approach-----")


def sort_lexo(my_string):
    words = my_string.split()
    words.sort()
    return words


my_string = "how are you ? had lunch ?"
print("after sorting:", sort_lexo(my_string))
print("--------4. using oops Approach---------")


class Sort:
    def __init__(self, str3):
        self.str3 = str3

    def get_input_string(self):
        print("input string:", self.str3)

    def get_sort_string(self):
        print("sort string:", sort_lexo(self.str3))


x = Sort("eating sugar no papa")
x.get_input_string()
x.get_sort_string()
