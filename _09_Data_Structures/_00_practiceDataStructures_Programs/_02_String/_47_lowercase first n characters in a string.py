'''
lowercase first n characters in a string

Topics
CRUD - retreive
data - string
state - input string
Behaviour - lowercase first n characters in string

# mathematical approach
step1 - get the input data
step2 - check the input data and lowercase first n characters in string
step3 - return the output to console

'''
print("--------1.using Builtin Approach-------")
str1 = 'PYTHON PROGRAMMING LANGUAGE'
print(str1[:4].lower() + str1[4:])

print("--------2.using Algorithm Approach-----")
string = "CHARACTERS"
for i in string:
    output = (string[:4].lower() + string[4:])
print("input string:", string)
print("lowercase first n characters:", output)
print("--------3.using functions Approach-----")
string = "KINGDOM"
st1 = "PYTHON PROGRAMMING LANGUAGE"


def lowercase(x):
    result = (x[:6].lower() + x[6:])
    return result


print("input string:", string)
print("lowercase first 6 :", lowercase(string))
print("input string:", st1)
print("lowercase first 6 ", lowercase(st1))
print("--------4. using oops Approach---------")


class Lower:
    def __init__(self, str1):
        self.str1 = str1

    def get_inputstring(self):
        print("input string:", self.str1)

    def get_lowercase(self, n):
        print("After converting:", (self.str1[:n].lower() + self.str1[n:]))


s1 = Lower("WELCOME TO PYTHON")
n = 7
s1.get_inputstring()
s1.get_lowercase(n)