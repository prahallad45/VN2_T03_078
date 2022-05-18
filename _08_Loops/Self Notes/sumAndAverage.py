n=int(input("ENTER HOW MANY NUMBER YOU WNAT TO FIND SUN AND AVG:"))
if(n<=0):
    print("INVALID  INPUT")
else:
    l=list()
    for i in range(1,n+1):
        val=float(input("ENTER THE VALUE:"))
        l.append(val)
    else:
        print("CONTENT OF L={}".format(l))
        s=0
        for i in l:
            s=s+i
        print("SUM ={}".format(s))
        print("AVERAGE={}".format(s/len(l)))