'''
# Sort unique words alphanumerically
Topics
CRUD - update
Type - String
state - input string
Behaviour - sort unique words in alphabets

# mathematical approach
step1- get the input data
step2- check the input string and sort in alphabet order
step3- return the output in console

'''
print("1.using Builtin Approach")
str = "124g1a0121 manikanta"
new_str = sorted(str)
print("input string:", str)
print("after sorting:", new_str)
print("2.using Algorithm Approach")
print("input string:", str)
for i in str:
    print("after sorting:", sorted(str))
print("3.using functions Approach")


def sort():
    result = sorted(string)
    return result


string = "simha the lion 123"
print("input string:", string)
print("after sorting:", sort())
print("4. using oops Approach")


class Sorting:
    def __init__(self, str1):
        self.str1 = str1

    def get_inputstring(self):
        print("input string:", self.str1)

    def get_sortedstring(self):
        print("sorted string:", sorted(self.str1))


y = Sorting("vaathi coming 96522")
y.get_inputstring()
y.get_sortedstring()