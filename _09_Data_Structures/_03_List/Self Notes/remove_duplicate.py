lst = [1,1,4,6,3,1,4,7,3,8]

res = []
for i in lst:
    if i not in res:
        res.append(i)
 
print (res)


# using function
def dup(lst):
    res = []
    for i in lst:
        if i not in res:
            res.append(i)
    return res
    
lst = [1,1,4,6,3,1,4,7,3,8]
print(dup(lst))