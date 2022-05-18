'''
# Create html from string
Topics
CRUD - update
Type - String
state - input string
Behaviour - update string html tag

# mathematical approach
step1- get the input data
step2- check the input string and update html tag
step3- return the output in console



'''
print("1.using Builtin Approach")
str = "welcome to python"
tag = "k"
html_string = "<%s>%s<%s>" % (tag, str, tag)
print("Html string:", html_string)

print("2.using Algorithm Approach")
string = "manikanta"
tag = "m"
for i in string:
    result = "<%s>%s</%s>" % (tag, string, tag)
print("after creating html string:", result)


print("3.using functions Approach")


def add_tags(tag, word):
    result = "<%s>%s</%s>" % (tag, word, tag)
    return result


print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))
print("4. using oops Approach")


class Tag:
    def __init__(self, string):
        self.string = string

    def get_inputstring(self):
        print("input string:", self.string)

    def get_htmlstring(self):
        print("HTML string:", add_tags("l", self.string))


x = Tag("raja the great")
x.get_inputstring()
x.get_htmlstring()
