n=int(input("ENTER HOW MANY NUMBER YOY WANT TO INPUT:"))
if(n<=0):
    print("INVALID  INPUT")
else:
    l=list()
    for i in range(1,n+1):
        val=int(input("ENTER THE VALUE:"))
        l.append(val)
    else:
        print(l)
        sec=int(input("ENTER WHICH NUMBER YOU WANT TO SEARCH:"))
        l.index(sec)
        print("{} IS PRESENT".format(sec))
       
