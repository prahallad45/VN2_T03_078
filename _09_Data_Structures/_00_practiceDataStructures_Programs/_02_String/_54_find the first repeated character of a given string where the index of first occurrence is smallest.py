'''
# find the first repeated character of a given string where the index of first occurrence is smallest
Topics
CRUD - retreive
data - string
state - input string
Behaviour - first repeated character in given string smallest index

# mathematical approach
step1 - get the input data
step2 - check the input data and first repeated character in given string smallest index
step3 - return the output to console

'''
print("--------1.using Builtin Approach-------")


print("--------2.using Algorithm Approach-----")

print("--------3.using functions Approach-----")


def first_repeated_char_smallest_distance(str1):
    temp = {}
    for ch in str1:
      if ch in temp:
        return ch, str1.index(ch);
      else:
        temp[ch] = 0
    return 'None'


print(first_repeated_char_smallest_distance("welcome"))
print(first_repeated_char_smallest_distance("abcb"))
print(first_repeated_char_smallest_distance("abcc"))
print(first_repeated_char_smallest_distance("abcxxy"))
print(first_repeated_char_smallest_distance("abc"))
print("____4.using oops Approach_____")


class First:
    def __init__(self, str):
        self.str = str

    def get_input(self):
        print("input string:", self.str)

    def get_firstrepeat(self):
        print("first repeat string:", first_repeated_char_smallest_distance(self.str))


p = First("manikanta")
p.get_input()
p.get_firstrepeat()



