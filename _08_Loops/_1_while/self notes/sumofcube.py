#SUM OF CUBE NUMBER
n=int(input("ENTER A NUMBER:"))
if(n<=0):
    print("INVALID INPUT")
else:
    i=1
    s=0
    while(i<=n):
        s=s+i**3
        print(i**3)
        i=i+1
    else:
        print("sum of CUBE {} is ".format(s))
