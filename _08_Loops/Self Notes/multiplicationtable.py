#MULTIPLICATION TABLE
n=int(input("ENTER A NUMBER:"))
if(n<=0):
    print("INVALID NUMBER")
else:
    for i in range(1,11):
        print("{}x{}={}".format(n,i,n*i))