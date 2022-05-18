#1 dynamic way using len()
str1=input("Enter a string:")

print(len(str1))


#2 using for loop
str2=input("enter a string:")
c=0
for x in str2:
    c+=1
print(c)

#3 using function
def findLen(str1):
    counter = 0    
    for i in str1:
        counter += 1
    return counter
  
str1 =input("Enter the string:")
print(findLen(str1))

#4 using class
class findfun:
    def __init__(self,x):
        self.x = x
    def show(self):
        c=0
        for i in self.x:
            c += 1
        print(c)

p=findfun("prahallad")
p.show()


