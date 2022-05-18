# P06. REQ : Remove odd index in a string
print("=====Remove odd index in string====")
'''
types:
CRUD : retrieve
data type : string
state: string
behaviour : Remove odd index

# mathematical approach
step 1 : check each element in a string
step 2 : remove the odd index in a string
step 3 : return the result
'''
print("___1.using Builtin approach___")
str1 = "manikanta"
print("input string:", str1)
print("after removing odd index values: ", str1[0], str1[2], str1[4], str1[6], str1[8])
print("____2.using algorithm approach____")
str = "welcome to the party"
for i in range(len(str)):
    if i % 2 != 0:
        print("after remove odd values:", str[i])
        i += 1


print("___3.using functions approach____")


def odd_values_string(str):
    result = ""
    for i in range(len(str)):
        if i % 2 != 0:
            result = result + str[i]
    return result


print("after removing odd value string:", odd_values_string("manikanta"))

print("_____4.using oops approach____")

class Odd:

    def __init__(self, str):
        self.str = str

    def get_string(self):
        print("input string:", self.str)

    def get_removeoddindex(self):
        for x in range(len(self.str)):
            if x % 2 != 0:
                print("after removing odd index:", self.str[x])
                x += 1


s1 = Odd("welcome to the party")
s1.get_string()
s1.get_removeoddindex()


















