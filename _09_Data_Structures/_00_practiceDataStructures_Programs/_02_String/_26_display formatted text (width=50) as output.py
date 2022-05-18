'''
# display formatted text (width=50) as output

Topics
CRUD - update
Type - String
state - input string
Behaviour - format text with width = 50

# mathematical approach
step1- get the input data
step2- check the input string and format the text
step3- return the output in console
'''
print("--------1.using Builtin Approach-------")
import textwrap
string = "Python is a widely used high-level language"
print("format text width 50:", textwrap.fill(string, width=50))

print("--------2.using Algorithm Approach-----")
for i in string:
    result = textwrap.fill(string, width=50)
print("after format text:", result)
print("--------3.using functions Approach-----")


def format():
    result = textwrap.fill(string, width=50)
    return result


print("after format the text:", format())
print("--------4. using oops Approach---------")


class Format:
    def __init__(self, string):
        self.string = string

    def get_input_string(self):
        print("input string:", self.string)

    def get_format_string(self):
        print("format string:", textwrap.fill(self.string, width=50))


t = Format("he is coming by tomorrow")
t.get_input_string()
t.get_format_string()
