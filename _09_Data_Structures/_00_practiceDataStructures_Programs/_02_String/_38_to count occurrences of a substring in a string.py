'''
# to count occurrences of a substring in a string
topics
CRUD - retrieve
Type- string
state - input string
Behaviour - return the count of substring in a input string

# mathematical approach
step1- get the input string
step2- check the string with substring and returns the count
step3- print the count of substring in console
'''
print("___1.Builtin function approach___")
x = "i saw a saw i never saw such a saw "
str1 = x.split()
str2 = str1.count("saw")
print("count of saw substring in string: ", str2)
print("___2.using algorithm approach___")
str = "make a meal with make a deal,make make the making"
for i in range(len(str)):
    result = (x.split(str))
print("count of substring:", str.count("make"))
print("____3.using functions approach____")
def count(x):
    result = x.split()
    return result


print("count of substring make in string:", str.count("make"))
print("____4.using oops approach____")
class Count:
    def __init__(self, str1):
        self.str1 = str1

    def get_inputstring(self):
        print("input string:", self.str1)

    def get_countstring(self):
        print("split of substring:", self.str1.split())
        print("count of the substring:", self.str1.count("the"))


s1 = Count("the wall will be the fall, fall the fall")
s1.get_inputstring()
s1.get_countstring()