#ACCEPT LIST OF NUMBER AND DISPLAY THE MULTIPLICATION TABLE FOR ALL THOSE VALUES
print("ENTER VALUE SEPERATED BY SPACE:")
n=[int(val)for val in input().split(" ")]  #LIST COMPREHENSASTION
print("CONTENT OF LIST={}".format(n))
for i in n:
    if(i<=0): #TO CHECH IF I VALUE IS 0 OR LESS THEN 0(-VE)
        print("{} IS INVALID INPUT".format(i))
    else:
        print("MULTIPLICATION FOR {}".format(i))
        for j in range(1,11):
            print("\t{}x{}={}".format(i,j,i*j))
