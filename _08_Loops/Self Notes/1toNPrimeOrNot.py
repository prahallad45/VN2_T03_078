n=int(input("ENTER A NUMBER:"))
if(n<=0):
    print("INVALID NUMBER")
else:
    for i in range(1,n+1):
        result=True
        for j in range(2,i):
            if(i%j==0):
                result=False
                break
        if(result):
            print("{} is prime".format(i))
        else:
            print("{} is not prime".format(i))
