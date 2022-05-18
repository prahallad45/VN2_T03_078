'''
# find the first non-repeating character in given string
Topics
CRUD - retreive
data - string
state - input string
Behaviour - first non-repeating character in given string

# mathematical approach
step1 - get the input data
step2 - check the input data and first non-repeating character in given string
step3 - return the output to console

'''
print("--------1.using Builtin Approach-------")


print("--------2.using Algorithm Approach-----")

print("--------3.using functions Approach-----")
NO_OF_CHARS = 256


def getcharcountarray(string):
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)] += 1
    return count


def firstnonrepeating(string):
    count = getcharcountarray(string)
    index = -1
    k = 0

    for i in string:
        if count[ord(i)] == 1:
            index = k
            break
        k += 1

    return index


string = "welcome"
index = firstnonrepeating(string)
if index == 1:
    print("Either all characters are repeating or string is empty")
else:
    print("First non-repeating character is " + string[index])



