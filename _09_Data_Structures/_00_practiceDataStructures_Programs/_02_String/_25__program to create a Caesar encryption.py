'''
# program to create a Caesar encryption
Topics
CRUD - create
Type - String
state - input string
Behaviour - create caeser encryption

# mathematical approach
step1- get the input data
step2- check the input string and create caeser encryption
step3- return the output in console

'''
print("--------1.using Builtin Approach-------")


print("--------2.using Algorithm Approach-----")
string = "acharya"
step = 2
outtext = []
crypttext = []
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
for eachLetter in string:
    if eachLetter in uppercase:
        index = uppercase.index(eachLetter)
        crypting = (index + step) % 26
        crypttext.append(crypting)
        newletter = uppercase[crypting]
        outtext.append(newletter)
    elif eachLetter in lowercase:
        index = lowercase.index(eachLetter)
        crypting = (index + step) % 26
        crypttext.append(crypting)
        newletter = lowercase[crypting]
        outtext.append(newletter)
print("input string:", string)
print("After crypting 2 steps", outtext)
print("--------3.using functions Approach-----")


def caesar_encrypt(realtext, step):
    outtext = []
    crypttext = []

    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

    for eachLetter in realtext:
        if eachLetter in uppercase:
            index = uppercase.index(eachLetter)
            crypting = (index + step) % 26
            crypttext.append(crypting)
            newletter = uppercase[crypting]
            outtext.append(newletter)
        elif eachLetter in lowercase:
            index = lowercase.index(eachLetter)
            crypting = (index + step) % 26
            crypttext.append(crypting)
            newletter = lowercase[crypting]
            outtext.append(newletter)
    return outtext


print("input string :", "welcome")
print("after encrypting:", caesar_encrypt("welcome", 2))
print("after encrypting: ", caesar_encrypt("welcome", 3))
print("after encrypting 5 steps:", caesar_encrypt("welcome", 5))
print("--------4. using oops Approach---------")


class Encrypt:
    def __init__(self, str1):
        self.str1 = str1

    def get_inputstring(self):
        print("input string:", self.str1)

    def get_sortstring(self):
        print("sorted string:", caesar_encrypt(self.str1, 3))


s = Encrypt("manikanta")
s.get_inputstring()
s.get_sortstring()