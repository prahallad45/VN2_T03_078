
# P04. REQ : Find length of longest string   ie., "once upon a time there was a king in mughal kingdom"
print("=====length of the longest string====")
'''
types:
CRUD : retrieve
data type : string
state: "once upon a time there was a king in mughal kingdom"
behaviour : length of longest string

1.mathematical approach

step 1: count each word
step 2: returns the number elements in ech word
step 3: then return the result of highest number of elements in  word
'''
print("_____1.built in approach_______")

list1 = ["aruna", "nani", "praveena"]
res = max(list1, key=len)
print("longest string", res)

print("____2.using algorithm approach_____")
max_len = -1
for x in list1:
    if len(x) > max_len:
        max_len = len(x)
        result = x
print("longest string:", result)

print("____3.using functions approach___")
tup = ("mani", "aditya", "varmaan")
def long():
    res = max(tup)
    return res
print("longest string:", max(tup, key=len))
print("____4.using oops approach____")


class Long:
    def __init__(self, input):
        self.input = input

    def get_string(self):
        print("input string:", self.input)

    def get_longeststring(self):
        print("longest string:", max(self.input, key=len))


s = Long(("mani", "welcome", "rajarama"))
s.get_string()
s.get_longeststring()
