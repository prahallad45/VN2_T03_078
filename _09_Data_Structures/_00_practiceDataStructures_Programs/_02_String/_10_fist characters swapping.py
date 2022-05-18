# P04. REQ : First last chars swapping in a string   ie., "once upon a time in mughal kingdom"
print("=====First characters swapping in string====")
'''
types:
CRUD : retrieve
data type : string
state: "once upon a time there was a king in mughal kingdom"
behaviour : first characters swapping

# mathematical approach
step 1 : check each word elements in given string
step 2 : convert the first elements of each word
step 3 : return the result
'''
print("__2.using Builtin approach___")

x = input("Enter the string :",)
print("First character swapped :", x.capitalize())

print("____3.using algorithm approach____")
for i in x:
    print("1st character swapped", x.capitalize())
print("____4.using functions approach_____")


def swap():
    result = x.capitalize()
    return result


print("after swapping of first character:", x.capitalize())
print("____5.using oops approach____")


class Swap:
    def __init__(self, str1):
        self.str1 = str1

    def get_string(self):
        print("input string:", self.str1)

    def get_swapstr(self):
        print("after swapping:", self.str1.capitalize())


s = Swap("manikanta")
s.get_string()
s.get_swapstr()




