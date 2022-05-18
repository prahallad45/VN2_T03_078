'''
# split a string on the last occurrence of the delimiter
Topics
CRUD - update
data - string
state - input string
Behaviour - split a string on last occurrence of delimiter

# mathematical approach
step1 - get the input data
step2 - check the input data and split the string on last occurrence of delimiter
step3 - return the output to console

'''
print("--------1.using Builtin Approach-------")
test_string = "gfg, is, good, better, and best"

# printing original string
print("The original string : " + str(test_string))
res = test_string.rsplit(', ', 1)
print("after splitting at last delimiter : " + str(res))

print("--------2.using Algorithm Approach-----")
string = "welcome, to, python, programming language"
for i in string:
    output = string.rsplit(',', 1)
print("input string:", string)
print("agter splitting at last delimiter:", output)
print("--------3.using functions Approach-----")
st1 = "PYTHON, PROGRAMMING, LANGUAGE"


def rsplit(x):
    result = x.rsplit(',', 2)
    return result


print("input string:", st1)
print("after split last delimiter", rsplit(st1))
print("--------4. using oops Approach---------")


class Rsplit:
    def __init__(self, str1):
        self.str1 = str1

    def get_inputstring(self):
        print("input string:", self.str1)

    def get_lastdelimiter(self, n):
        print("After converting:", self.str1.rsplit(',', n))


s1 = Rsplit("the quick brown fox, jump over, lazy dog")
n = 1
s1.get_inputstring()
s1.get_lastdelimiter(n)