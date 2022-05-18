
'''
# P03. REQ : Find String slicing   ie., "kukatpally jntu"

types:
CRUD : Retrieve
data type: string
state : kuktpally jntu
behaviour: slicing

_01 mathematical approach

'''
print("___2.using builtin approach___")
k = "kukatpally jntu"
print(k[1:2])
print("sliced string :", k[1:5])
print(" sliced string :", k[5:12])

print("_____3.using algorithm approach____")
k = "kukatpally jntu"
for var in k:
    print("sliced string :", k[0:15])

print("___4.using functions approach____")
str = input("enter the string:")


def slice():
    result = str.slice()
    return result


print("after slicing of string:", str[1:5])
print("___5.using oops approach____")
class Slice:
    def __init__(self, str):
        self.str = str

    def get_string(self):
        print("get input string:", self.str)

    def get_slice(self):
        print("after slicing :", self.str[1:5])


v = Slice("maniknat")
v.get_string()
v.get_slice()