'''
# Replace first occurrence character
Topics
CRUD - Update
type - string
state - input string
Behaviour - replace the first occurrence

# mathematical approach
step 1: get the input string
step 2: check the input string and replace
step 3: return the output

'''
print("1.using builtin approach")
string = "manikanta"
new_str = string.replace("m", "M")
print("input string:", string)
print("After replace the first character in string:", new_str)
print("2.using Algorithm approach")
for var in string:
    print("input string:", string)
    print("after replace:", string.replace("n", "N"))
print("3.using Functions approach")


def replace():
    result = string.replace("k", "Ka")
    return result


print("input string:", string)
print("after replace:", replace())
print("4.using oops approach")


class Replace:
    def __init__(self, string):
        self.string = string

    def get_inputstring(self):
        print("input string:", self.string)

    def get_replcestring(self):
        print("replace string:", self.string.replace("a", "AA"))


s1 = Replace("warrior")
s1.get_inputstring()
s1.get_replcestring()