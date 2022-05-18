'''
# find the first repeated word in a given string
Topics
CRUD - retrieve
data - string
state - input string
Behaviour - find the first repeated word in a given string

# mathematical approach
step1 - get the input data
step2 - check the input data and find the first repeated word in a given string
step3 - return the output to console

'''
print("--------1.using Builtin Approach-------")


print("--------2.using Algorithm Approach-----")

print("--------3.using functions Approach-----")


def first_repeated_word(str1):
    temp = set()
    for word in str1.split():
      if word in temp:
        return word;
      else:
        temp.add(word)
    return 'None'


print(first_repeated_word("i saw movie which is one of good movie"))


print("____4.using oops Approach_____")


class Word:
    def __init__(self, str):
        self.str = str

    def get_input(self):
        print("input string:", self.str)

    def get_firstrepeatword(self):
        print("first repeat string:", first_repeated_word(self.str))


w = Word("he is working and he is good")
w.get_input()
w.get_firstrepeatword()