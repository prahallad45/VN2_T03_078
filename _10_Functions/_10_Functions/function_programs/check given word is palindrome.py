'''
palindrome means word should be same from left to right or right to left
eg: madam, xerox,redivider,deified, civic, radar, level, rotor, kayak, reviver, racecar, madam, and refer

# Check given word is palindrome or not

TOPICS
CRUD - Retreive
Data type - string
state - input string
behaviour - check word is palindrome or not

'''
print("---using functions approach----")

str = "madam"


def ispalindrome(str):
    result = str[::-1]
    return result


if str == ispalindrome(str):
    print("after checking string : yes")
else:
    print("no")
