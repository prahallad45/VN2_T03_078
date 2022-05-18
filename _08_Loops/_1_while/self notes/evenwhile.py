#WAP WHICH WILL DISPLAY EVEN NUMBER WITH IN N WHERE N MUST BE +VE INTEGER VALUE
n=int(input("ENTER A NUMBER:"))
if(n<=0):
    print("invalid input")
else:
    i=2
    while(i<=n):
        print(i)
        i=i+2