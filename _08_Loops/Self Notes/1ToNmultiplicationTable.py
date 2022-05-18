#DILPLAY MULTIPLICATION TABLE 1 TO N
n=int(input("ENTER A NUMBER:"))
if(n<=0):
    print("INVALID NUMBER")
else:
    for i in range(1,n+1):
        for j in range(1,11):
            print("\t{}x{}={}".format(i,j,i*j))
        print("*"*40)