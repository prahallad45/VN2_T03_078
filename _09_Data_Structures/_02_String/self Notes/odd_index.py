#using loops
str="sachin Tendulkar"
res = "" 
for i in range(len(str)):
    if i % 2 != 0:
      res = res + str[i]
print(res)


#using function
def odd_str(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 != 0:
      result = result + str[i]
  return result

print(odd_str('viratkohli'))
