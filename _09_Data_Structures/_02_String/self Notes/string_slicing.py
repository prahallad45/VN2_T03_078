#1 simple way for slicing
str1 = "Rohit Sharma"

print(str1[:5]) #it will print 0 index to 4 index 

#2 using for loop
str2="Sachin Tendulkar"
for x in str2[:10]:
    print(x)

#3 using function
def slicing(str3):   
    for i in str3[3:10]: #it will print from 3th index to 9th index only
        print(i)
        
  
str3 =input("Enter the string:")
slicing(str3)

#4 using class 
class slicing:
    def __init__(self,x):
        self.x=x

    def show(self):
        print(self.x[:10]) #it will print from start to 9 index
pg=slicing("salman khan")
pg.show()


