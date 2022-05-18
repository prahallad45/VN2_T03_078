'''
# program to remove a newline in Python

Topics
CRUD - Delete
datatype - string
state - input string
Behaviour - remove new line

# arthimetic approach
step 1 = get input from user
step 2 = check new line in program
step 3 = remove new line

'''
print("____2.Builtin approach___")

str1 = "\n starbucks has the best coffe \n"
str2 = str1.strip()
print("after removing new line:", str2)

print("___3.algorithm approach___")

list1 = ["\nstarbucks", "has the best\n", "coffee \n."]
list2 = []

for var in list1:
    list2.append(var.replace("\n", ""))
print("New list:" + str(list2))

print("____4.using functions____")

str1 = "starbucks has a good coffee \n"


def strip():
    result = str1.strip()
    return result


print("after removing new line:", str1.strip())

print("____5 using oops____")
class Strip:

    def __init__(self, str1):
        self.str1 = str1

    def get_string(self):
        print("After removing new line:", self.str1)


str1 = "\n hardrock rock cafe has good coffee \n"
s1 = Strip(str1.strip())
s1.get_string()