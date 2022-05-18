#simple way
str1="ramesh"
s = str1[0]
e = str1[-1]
      
swapstr = e + str[1:-1] + s
print(swapstr)

#using function
def swap(string):
    start = string[0]
    end = string[-1]
      
    swapstr = end + string[1:-1] + start
    print(swapstr)
swap("prahallad")

