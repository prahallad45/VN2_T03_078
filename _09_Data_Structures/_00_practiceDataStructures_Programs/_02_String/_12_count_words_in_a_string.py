# P07. REQ : count words in a string
'''
Types
CRUD : Retrieve
data type: string
state : given string
behaviour :count words in given string

# mathematical approach
step 1: check each word in given string
step 2: count words in string
step 3: Return the number of count
'''

print("___2.using Built in approach___")
x = "Twinkle Twinkle little star " \
    "how i wonder what you are " \
    "up above the word so high " \
    "like a diamond in the sky"
print("The original string:", x)
new_str = len(x.split())
print("count of words in string:", new_str)

print("___3.using algorithm approach____")
x = "mani good"
for i in x:
    print("count of words:", len(x.split()))

print("____4.using function approach___")


def split(str):
    result = len(str.split())
    return result


print("count of words:", split("nani is too damn and natural"))

print("___5.using oops approach____")


class Split:
    def __init__(self, str):
        self.str = str

    def get_string(self):
        print("input string:", self.str)

    def get_count(self):
        print("count of string:", len(self.str.split()))


s1 = Split("welcome to python programming language")
s1.get_string()
s1.get_count()