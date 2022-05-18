#simple way
str1 = 'Rohit sharma'
print(str1.upper())
print(str1.lower())

#using function
def upper_lower(str2):
    print(str2.upper())
    print(str2.lower())
   
upper_lower("he is a boy")

#using class
class upperlower:
    def __init__(self,x):
        self.x = x
    def show(self):
        print(self.x.upper())
        print(self.x.lower())

p=upperlower("prahallad")
p.show()
