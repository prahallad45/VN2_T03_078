'''
# capitalize first and last letters of each word of a string
Topics
CRUD - update
Type - string
State - input string
Behaviour - capitalize first and last letters

# mathematical approach
step 1: get the input data
step 2: check the input string and capitalize the first and last letters of each word
step 3: return the output
'''

print("1.using the Builtin approach")
str = "they are going to movie"
str2 = str.capitalize()
print(str2)

print("2.using algorithm approach")
str1 = "phani got job"
str1 = result = str1.title()
result = ""
for word in str1.split():
    result += word[:-1] + word[-1].upper() + " "
    print("After capitalize:", result[:-1])

print("3.using functions approach")


def capitalize_first_last_letters(str1):
    str1 = result = str1.title()
    result = ""
    for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
    return result[:-1]


print("after capitalize:", capitalize_first_last_letters("python exercises practice solution"))
print("4.using oops approach")


class Capitalize:
    def __init__(self, str):
        self.str = str

    def get_inputstring(self):
        print("input string:", self.str)

    def get_updatedstring(self):
        print('after capitalize:', capitalize_first_last_letters(self.str))


str1 = Capitalize("they ate food in restaurant")
str1.get_inputstring()
str1.get_updatedstring()