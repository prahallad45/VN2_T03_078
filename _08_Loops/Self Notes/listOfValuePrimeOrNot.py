#ACCEPT LIST OF VALUE AND DECIDE WHETHER IT IS PRIME OR NOT
print("ENTER VALUE SEPERATED BY SPACE:")
lst=[int(val)for val in input().split(" ")]  #LIST COMPREHENSASTION
print("CONTENT OF LIST={}".format(lst))
for n in lst:
    if(n<=0): #TO CHECH IF I VALUE IS 0 OR LESS THEN 0(-VE)
        print("{} IS INVALID INPUT".format(n))
    else:
        result=True
        for i in range(2,n):
            if(n%i==0):
                result=False
                break
        if(result==True):
            print("{} is prime".format(n))
        else:
            print("{} is not prime".format(n))

