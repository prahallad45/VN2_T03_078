'''

# convert a given string into upper case

Topics
CRUD - RETRIEVE
data type - string
state - input string
behaviour - convert into uppercase

# 1.Arthemetic approch
step1- get the input string
step2 - convert into uppercase format

'''

print("___2.Builtin Approach___")
str = input("Enter the string:")
str1 = str.upper()
print("after converting the string:", str1)

print("____3.algorithm approach___")
str = input("Enter the string:")
le = 0
for var in str:
    le += 1
    print("After converting the string:", str.upper())

print("____4.using functions approach____")
str = input("Enter the string:")


def upper(str):
    result = upper(str)
    return result


print("after converting the string:", str.upper())
print("____5.using oops____")


class String:

    def __init__(self, str):
        self.str = str

    def get_string(self):
        print("convert the string into uppercase:", self.str)


str = input("Enter the string:")
s1 = String(str.upper())
s1.get_string()
