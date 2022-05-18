def r(lst):

    for i in lst:
        if i%2==0:
            lst.remove(i)
    print(lst)
    
lst = [1,1,4,3,1,4,7,3,8]
r(lst)