#1 dynamic way using count() to count the occurance of a in the string
str1=input("Enter a string:")

print(str1.count("a"))


#2 using for loop
str2=input("enter a string:")
c=0
for x in str2:
    if x == 'a':
        c+= 1
print(c)

#3 using function
def findocc(str1):
    counter = 0    
    for i in str1:
        if i == 'a':
            counter += 1
    return counter
  
str1 =input("Enter the string:")
print(findocc(str1))

#4 using class
class findfun:
    def __init__(self,x):
        self.x = x
    def show(self):
        c1=0
        for i in self.x:
            if i == 'a':
                c1 += 1
        print(c1)

p=findfun("prahallad")
p.show()


