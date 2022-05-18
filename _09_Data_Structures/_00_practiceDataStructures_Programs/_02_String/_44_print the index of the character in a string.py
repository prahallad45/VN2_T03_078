'''
print the index of the character in a string

Topics
CRUD - retreive
data - string
state - input string
Behaviour - print the index of character in a string

# mathematical approach
step1 - get the input data
step2 - check the input data and print the index character in a string
step3 - return the output to console

'''
print("--------1.using Builtin Approach-------")
string = "infinite"
str = string.find("n")
print("index of n:", str)

print("--------2.using Algorithm Approach-----")
string = "characters"
for i in string:
    output = string
print("input string:", string)
print("index character a in string:", output.find("a"))
print("--------3.using functions Approach-----")
string = "kingdom"


def func(x):
    result = string.find(x)
    return result


print("input string:", string)
print("After strip of characters:", func("o"))
print("--------4. using oops Approach---------")


class Index:
    def __init__(self, str1):
        self.str1 = str1

    def get_inputstring(self):
        print("input string:", self.str1)

    def get_index(self, n):
        print("index of character:", self.str1.find(n))


s1 = Index("welcome to python")
s1.get_inputstring()
s1.get_index("y")