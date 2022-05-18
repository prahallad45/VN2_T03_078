'''
# program to check whether a string starts with specified characters

Topics
CRUD - retrieve
datatype = string
state = input
Behaviour = startwith()

# 1. Arthmetic approach:
step 1. get input from user
step 2..check string start with special characters
'''

print("____2.Builtin approach______")
str1 = input("Enter the string:")
str2 = str1.startswith("@,$,#,$,%,^,&,*", 0, len(str1))
print("After checking :", str2)

print("____3.Algorithm approach___")
str1 = input("Enter string :")
for var in str1:
    print("after checking:", str1.startswith("@, $, #, $, %, ^, &, *", 0, len(str1)))

print("___4.using functions approach___")
str1 = input("Enter string :")


def startswith():
    result = startswith()
    return result


print("After checking:", str1.startswith("@,#,$,%,^,&,*", 0, len(str1)))

print("___5.using oops____")


class Startswith:

    def __init__(self, str1):
        self.str1 = str1

    def get_string(self):
        print("after converting:", self.str1)


str1 = input("Enter string :")
s1 = Startswith(str1.startswith("@,#,$,%,^,&,*", 0, len(str1)))
s1.get_string()