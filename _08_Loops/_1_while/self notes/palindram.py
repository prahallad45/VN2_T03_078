#PROGRAM TO CHECK IT IS PALINDRAM OR NOTR
n=int(input("ENTER NUMBER: "))
if(n<=0):
    print("INVALID INPUT")
else:
    r=0
    while(n>0):
        d=n%10
        r=r*10+d
        n=n//10
    else:
        if(n==r):
            print("It is a palindram")
        else:
            print("It is not a palindram")