'''
# Insert string in middle of specical chars
Topics
CRUD - update
Type - String
state - input string
Behaviour - insert string

# mathematical approach
step1- get the input data
step2- check the input string and insert in between special chars
step3- return the output in console
'''
print("1.using Builtin Approach")
string = "Mani%%"
str2 = "mani"
new_str = string[:5]+str2+string[5]
print(new_str)
print("2.using Algorithm Approach")
str2 = "<<>>"
word = "john"
for i in str2:
    output = str2[:2] + word + str2[2:]

print("after inserting:", output)
print("3.using functions Approach")


def insert_string_middle(str, word):
    result = str[:2] + word + str[2:]
    return result


print("After inserting:", insert_string_middle('[[]]', 'Python'))
print("after inserting:", insert_string_middle('{{}}', 'PHP'))
print("after inserting:", insert_string_middle('<<>>', 'HTML'))
print("4. using oops Approach")


class Insert:
    def __init__(self, str3):
        self.str3 = str3

    def get_inputstring(self):
        print("input string:", self.str3)

    def get_insertstring(self):
        print("after inserting:", insert_string_middle('$@@$', self.str3))


s = Insert("welcome to python")
s.get_inputstring()
s.get_insertstring()







