'''
count and display the vowels of a given text
Topics
CRUD - Retrieve
type - String
state - input string
Behaviour - return count of vowels

# mathematical approach
step1- get the input data
step2- check the number of vowels in string
step3- return the count of vowels
'''

print("____1.using builtin approach___")
str1 = "manikanta good"
vowels = "A,E,I,O,U,a,e,i,o,u"
print("count of vowels:", str1.count(vowels, 0, len(str1)))

print("____3.using functions approach___")


def vowels_count(string, vowels):
    result = [each for each in string if each in vowels]
    print(len(result))
    return result


string = "game of Thrones"
vowels = "AEIOUaeiou"
print(vowels_count(string, vowels))

print("___4.using oops approach___")


class Count:
    def __init__(self, str):
        self.str = str

    def get_inputstring(self):
        print("input string:", self.str)

    def get_vowelcount(self):
        print(vowels_count(self.str, vowels))


s1 = Count("supreme hero")
s1.get_inputstring()
s1.get_vowelcount()