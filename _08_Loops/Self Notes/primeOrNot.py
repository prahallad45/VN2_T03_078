#ACCEPT A NUMBER AND CHECH WHETHER IT IS PRIME OR NOT
n=int(input("ENTER A NUMBER:"))
if(n<=0):
    print("INVALID INPUT")
else:
    i=1
    c=0
    for i in range(i,n+1):
        if(n%i==0):
            c=c+1
    else:
        if(c==2):
            print("IT IS A PRIME")
        else:
            print("IT IS NOT A PRIME")
