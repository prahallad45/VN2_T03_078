'''
# find the second most repeated word in a given string
Topics
CRUD - retrieve
data - string
state - input string
Behaviour - find the second most repeated word in a given string

# mathematical approach
step1 - get the input data
step2 - check the input data and find the first second most repeated word in a given string
step3 - return the output to console

'''
print("--------1.using Builtin Approach-------")


print("--------2.using Algorithm Approach-----")

print("--------3.using functions Approach-----")


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    counts_x = sorted(counts.items(), key=lambda kv: kv[1])
    # print(counts_x)
    return counts_x[-2]


print(word_count("i saw a movie such a movie never saw"))

print("____4.using oops Approach_____")


class Word:
    def __init__(self, str):
        self.str = str

    def get_input(self):
        print("input string:", self.str)

    def get_firstrepeatword(self):
        print("first repeat string:", word_count(self.str))


w = Word("he is smart working and he is good and smart")
w.get_input()
w.get_firstrepeatword()