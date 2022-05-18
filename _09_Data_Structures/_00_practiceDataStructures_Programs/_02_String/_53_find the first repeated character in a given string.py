'''
# find the first repeated character in a given string

Topics
CRUD - retreive
data - string
state - input string
Behaviour - first repeated character in given string

# mathematical approach
step1 - get the input data
step2 - check the input data and first repeated character in given string
step3 - return the output to console

'''
print("--------1.using Builtin Approach-------")


print("--------2.using Algorithm Approach-----")

print("--------3.using functions Approach-----")


def firstrepeatedchar(str):
    h={}
    for ch in str:
        if ch in h:
            return ch
        else:
            h[ch] = 0

    return '\0'


print(firstrepeatedchar("xerox"))

print("____4.using oops Approach_____")


class First:
    def __init__(self, str):
        self.str = str

    def get_input(self):
        print("input string:", self.str)

    def get_firstrepeat(self):
        print("first repeat string:", firstrepeatedchar(self.str))


s1 = First("manikanta")
s1.get_input()
s1.get_firstrepeat()
