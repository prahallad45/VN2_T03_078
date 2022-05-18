'''
count repeated characters in a string
Topics
CRUD - Retreive
data type - string
state - input string
behaviour - count repeated characters

# mathematical approach
step1 - get the input data
step2 - check any repeated characters in string and count the number
step3 - return the count
'''
print("___1.Arthemetic approach___")
chars = "abcdefghijklmnopqrstuvwxyz"

str3 = "manikanta"
count = str3.count(chars, 0, len(str3))
print("count of repeated characters in string:", chars, count)
print("____2.Algorithm approach_____")
string = "great responsibility"
chars = "abcdefghijklmnopqrstuvwxyz"
for chars in string:
    count = string.count(chars)
    if count > 1:
        print(chars, count, end=chars)


check_string = "manikanta"
count = {}
for s in check_string:
    if s in count:
        count[s] += 1
    else:
        count[s] = 1
    for key in count:
        if count[key] > 1:
            print("Repeated characters:", key, count[key])
print("___3.using functions approach___")


def repeated_count(string, chars):
    result = [each for each in string if each in chars]
    print(len(string))
    return result


string = "xerox"
chars = "abcdefghijklmnopqrstuvwxyz"
print("Repeated characters in string:", repeated_count(string, chars))




