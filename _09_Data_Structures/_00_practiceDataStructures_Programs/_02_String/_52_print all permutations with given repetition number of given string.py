'''
# print all permutations with given repetition number of given string

'''
from itertools import product
print("____3.using functions approach_____")


def all_repeat(str1, rno):
   chars = list(str1)
   results = []
   for c in product(chars, repeat=rno):
     results.append(c)
   return results


print(all_repeat('mani', 3))
print("____4.using oops approach___")


class Repeat:
    def __init__(self, str1):
        self.str1 = str1

    def get_input(self):
        print("input string:", self.str1)

    def get_repeat(self, n):
        print("repeat string:", all_repeat(self.str1, n))


s1 = Repeat("john")
n = 4
s1.get_input()
s1.get_repeat(n)