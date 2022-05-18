'''
# remove duplicate characters of a given string
Topics
CRUD - delete
Type - string
State - input string
Behaviour - remove duplicates from string

# mathematical approach
step 1: get the input data
step 2: check the input string and capitalize the first and last letters of each word
step 3: return the output
'''

print("1.using the Builtin approach")


print("2.using algorithm approach")


print("3.using functions approach")


def removeduplicate(str, n):
    # Used as index in the modified string
    index = 0

    # Traverse through all characters
    for i in range(0, n):

        # Check if str[i] is present before it
        for j in range(0, i + 1):
            if (str[i] == str[j]):
                break

        # If not present, then add it to
        # result.
        if (j == i):
            str[index] = str[i]
            index += 1

    return "".join(str[:index])


# Driver code
str = "manikanta"
n = len(str)
print(removeduplicate(list(str), n))
print("4.using oops approach")


class Duplicate:
    def __init__(self, str1):
        self.str1 = str1

    def get_input(self):
        print("input string:", self.str1)

    def get_removeduplicate(self, n):
        print("get duplicate remove string:", removeduplicate(list(self.str1), n))


s1 = "king in kingdom"
s = Duplicate("king in kingdom")
s.get_input()
n = len(s1)
s.get_removeduplicate(n)






