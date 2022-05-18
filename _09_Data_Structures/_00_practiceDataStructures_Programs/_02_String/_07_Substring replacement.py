'''
# Substring replacement
Topics
CRUD - update
type - string
state - input string
Behaviour - substring replacement

# mathematical approach
step1 - get the input data
step2 - check the input string nd replace the substring
step3 - return the output

'''
print("1.using Builtin Approach")
string = "i saw a saw i never saw such a saw"
new_str = string.replace("saw", "knife")
print("input string:", string)
print("after replace substring:", new_str)
print("2.using Algorithm Approach")
print("input string:", string)
for var in string:
    print("After replace:", string.replace("saw", "cut"))
print("3.using functions Approach")


def replace():
    result = string.replace("saw", "shoot")
    return result


print("input string:", string)
print("after replace:", replace())

print("4. using oops Approach")


class Replace:
    def __init__(self, str1):
        self.str1 = str1

    def get_inputstring(self):
        print("input string:", self.str1)

    def get_replacestring(self):
        print("replace string:", self.str1.replace("fear", "fire"))


s = Replace("i am here don't fear")
s.get_inputstring()
s.get_replacestring()
