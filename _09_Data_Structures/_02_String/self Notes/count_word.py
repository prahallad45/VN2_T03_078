#simple way
srt = "ram is playing football in the field"
print ("The original string is : " +  srt)
res = len(srt.split()) #it split entire string by space

print ("total nos of words are : " +  str(res))

#using function
def findword(srt):
    print(srt)
    res = len(srt.split())
    return res

a=findword("he is a boy")
print(a)
