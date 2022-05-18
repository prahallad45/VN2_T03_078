l1=[1,2,5,2,5]
l2=[2,5,7,22,88]
l3=[33,5,22,65]
lst=[]

for x in l1:
    if x not in lst:
        lst.append(x)

for x in l2:
    if x not in lst:
        lst.append(x)

for x in l3:
    if x not in lst:
        lst.append(x)

print(lst)
#------------------------------xxxxxxxxx-------------------
r=range(0,101)
n=int(input("Enter a number:"))

if n in r:
    print("in")
else:
    print("not in")

#------------------------------xxxxxxx---------------
number=[11,5,6,9,0]
for i in range(len(number)):
  for j in range(i+1,len(number)):
    if number[i]>number[j]:
      number[i],number[j]=number[j],number[i]
print(number)

