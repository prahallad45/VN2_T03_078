'''
check if a string contains all letters of the alphabet
Topics
CRUD - retrieve
data - string
state - input string
Behaviour - check string contain all alphabets

# mathematical approach
step1 - get the input data
step2 - check the input data contain all aplhabets
step3 - return the output to console

'''
print("--------1.using Builtin Approach-------")
import string
alphabet = set(string.ascii_lowercase)
input_string = 'The quick brown fox jumps over the lazy dog'
print(set(input_string.lower()) >= alphabet)
input_string = 'The quick brown fox jumps over the lazy cat'
print(set(input_string.lower()) >= alphabet)
input_string = "abcdefghijklmnopqrstuvwxyz"
print(set(input_string.lower()) >= alphabet)
print("--------2.using Algorithm Approach-----")
input_string = 'the quick brown fox jumps over the lazy dog'

for i in input_string:
    alphabet = set(string.ascii_lowercase)
print(set(input_string.lower()) >= alphabet)

print("--------3.using functions Approach-----")
string = "kingdom"


def func():
    alphabet = set(string.ascii_lowercase)
    return result


print("After checking:", set(input_string.lower()) >= alphabet)


print("--------4. using oops Approach---------")
