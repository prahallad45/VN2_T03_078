# print last part of string
'''
Topics
CRUD: Retrieve
DATA TYPE: string
STATE: input
Behaviour: str.removeprefix()
# 1.mathematical approach
step1 = get the input from user
step 2 = using removeprefix() method
'''
# 2 using builtin method
print("___Builtin method approach___")
str = "hello world"
print("last part of the string:", str.removeprefix("hello"))

# 3 using algorithm aproach
print("___using algorithm approach___")
count = 0
for var in str:
    count += 1
    print("last part of string :", str.removeprefix("hello"))
# 4 using functions
print("___using functions___")
# state:
str = "hello python"


def string():
    result = str
    return result
# behaviour:


print("last part of string:", str.removeprefix("hello"))
# 5 using oops
print("___using oops___")

str = "mani kanta"
# state:


class String:
    def __init__(self, str):
        self.str = str

    def myfunc(self):
        print("last part of the string:", self.str)


s1 = String(str.removeprefix("mani"))
s1.myfunc()


