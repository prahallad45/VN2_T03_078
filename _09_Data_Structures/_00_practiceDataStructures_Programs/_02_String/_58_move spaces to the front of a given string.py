'''
# move spaces to the front of a given string
Topics
CRUD - update
data type - string
state - input string
behaviour - move spaces to front

# mathemetical approach
step1 - get the input string
step2 - check the input string and any spaces move to front
step3 - return the output in console

'''
print("1.using builtin approach")
string = "mani kanta"
print("input string:", string)
print("2.using algorithm approach")
# initializing the string
string = "I am a python programmer."
# finding all character exclusing spaces
chars = [char for char in string if char != " "]
# getting number of spaces using count method
spaces_count = string.count(' ')
# multiplying the space with spaces_count to get all the spaces at front of the new_string
new_string = " " * spaces_count
# appending characters to the new_string
new_string += "".join(chars)
# printing the new_string
print("after moving the spaces:", new_string)


print("3.using functions approach")
string = "python programming language."


def remove_space(string):
    chars = [char for char in string if char != " "]
    spaces_count = string.count(' ')
    new_string = " " * spaces_count
    new_string += "".join(chars)
    return new_string


print("after removing spaces:", remove_space(string))
print("4.using oops approach")

class Remove:
    def __init__(self, str):
        self.str = str

    def get_inputstring(self):
        print("input string:", self.str)

    def get_removespace(self):
        print("remove space string:", remove_space(self.str))


s1 = Remove("dude can we catch up later")
s1.get_inputstring()
s1.get_removespace()
