'''
# to set the indentation of the first line

Topics :
CRUD : update
data type = string
state = input string
behaviour = set indentation


# Artimetic approach
step 1 = get the input string
step 2 = set the identation for first line
step 3 = return the updated string
'''

print("____2.Builtin approach___")
import textwrap
str1 = '''
Python is a widely used high-level, general-purpose, interpreted, dynamic
programming language. Its design philosophy emphasizes code readability,
and its syntax allows programmers to express concepts in fewer lines of
code than possible in languages such as C++ or Java.
'''

str2 = textwrap.dedent(str1).strip()

print()
print(textwrap.fill(str2,
                    initial_indent='',
                    subsequent_indent=' ' * 4,
                    width=80
                    ))
print()

print("using algorithm approach")
str = '''
Twinkle twinkle little star
like a diamond in the sky
up above the world so high
'''