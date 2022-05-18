#CALCULATE SUM OF 1ST N NATURAL NUMBER,SQUARE AND CUBE OF N 
n=int(input("ENTER A NUMBER:"))
if(n<=0):
    print("INVALID INPUT")
else:
    s=0
    sq=0
    cu=0
    i=1
    for i in range(1,n+1):
        
        s=s+i
        sq=sq+i**2
        cu=cu+i**3
        print("\t{}\t{}\t{}".format(i,i**2,i**3))
    print("-"*40)
    print("sum=\t{}\t{}\t{}".format(s,sq,cu))