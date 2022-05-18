#WAP WHICH WILL PRINT FACTORIAL OF A GIVEN NUMBER
n=int(input("ENTER A NUMBER:"))
if(n<=0):
    print("invalid input")
else:
    i=1
    while(i<n):
        if(n%i==0):
            print(i)
        i=i+1