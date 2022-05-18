'''
# nth index character from string
Topics
CRUD - Retrieve
Data type - string
state - input string
Behaviour - retreive nth index character

# mathematical approach
step1 - get the input string
step2 - check the nth character in input string
step3 - return the output of string

'''
print("1.using Builtin Approach")

string = "i bought a new home"
new_str = string[-1]
print("input sring:", string)
print("nth index character:", new_str)
print("2.using Algorithm Approach")
print("input string:", string)
for var in string:
    print("nth character:", string[-1])

print("3.using functions Approach")
def end():
    result = string[-1]
    return result
print("input string", string)
print("nth character:", end())
print("4. using oops Approach")


class Character:
    def __init__(self, string):
        self.string = string

    def get_inputstring(self):
        print("input string:", self.string)

    def get_endcharacter(self):
        print("nth character:", self.string[-1])


str = Character("twinkle twinkle little star")
str.get_inputstring()
str.get_endcharacter()
