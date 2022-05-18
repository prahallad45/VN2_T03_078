#WAP WHICH WILL GENERATE N TO 1 NUMBER WHERE N MUST BE +VE INTEGER VALUE
n=int(input("enter a number:"))
if(n<=0):
    print("invalid input")
else:
    i=1
    while(n>=i):
        print("value of i= {}".format(n))
        n=n-1