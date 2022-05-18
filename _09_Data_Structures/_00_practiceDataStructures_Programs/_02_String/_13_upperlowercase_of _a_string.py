# Upper lower case of a string

'''
# Topics
CRUD: update type
data type: string
state/ input: VolkswaGen

# 1 mathematical approach
step.1 = get input
step 2 = update the string with upperlower case
'''
# 2. Builtin method approach
print("____using Builtin method approach____")
str = "VolkswaGen"
str1 = str.swapcase()
print("after upper lower case of string:", str1)

# 3. Algorithm approach
print("____using algorithm approach____")
str = input("Enter ths string:")
count = 0
for var in str:
    count += 1
    print("upper lower case of string:", str.swapcase())

# 4.using functions
print("using functions approach")
# state
str = input("Enter ths string:")
# Behaviour


def swapcase(str):
    result = str.swapcaase()
    return result


print("swapcase of string:", str.swapcase())
# 5. using oops
print("____using OOPS____")
# state:

str = input("Enter the string:")


class String():
    def __init__(self, str):
        self.str = str

    def myfunc(self):
        print("upper lower case of string:", self.str)
# Behaviour/ object


s1 = String(str.swapcase())
s1.myfunc()
