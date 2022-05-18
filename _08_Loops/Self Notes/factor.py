#FACTOR OF A GIVEN NUMBER USING FOR LOOP
n=int(input("ENTER A NUMBER:"))
if(n<=0):
    print("INVALID INPUT")
else:
    for i in range(1,n):
        if(n%i==0):
            print(i)
       
        