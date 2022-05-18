'''
# that accepts a string and calculate the number of digits and letters

Topics
CRUD - Retrieve
data - string
state - input string
Behaviour - calculate the numbers and letters in a string

# mathematical approach
step1 - get the input data
step2 - check the input data and calculate the numbers and letters in a string
step3 - return the output to console

'''
print("--------1.using Builtin Approach-------")
string = "mani 124"
new_str = string.isnumeric()

print("input string:", string)
print("after calculate the letters in string:", new_str)
print("--------2.using Algorithm Approach-----")
s = "king have 965220 dollars"
d = l = 0
for c in s:
    if c.isdigit():
        d = d+1
    elif c.isalpha():
        l = l+1
    else:
        pass
print("Letters", l)
print("Digits", d)


print("--------3.using functions Approach-----")

print("--------4. using oops Approach---------")
