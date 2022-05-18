#PRINT ODD NUMBER FROM N TO 1
n=int(input("ENTER A NUMBER:"))
if(n<=0):
    print("INVALID NUMBER")
else:
    i=0
    for n in range(n,i,-1):
        if(n%2!=0):
            print(n)
