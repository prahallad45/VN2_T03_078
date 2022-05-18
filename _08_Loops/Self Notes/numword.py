n=int(input("ENTER A NUMBER:"))
r=0
while(n>0):
    d=n%10
    r=r*10+d
    n=n//10
else:
    while (r>0):
        d=r%10
        match d:
            case 0:
                print("ZERO",end=" ")
            case 1:
                print("ONE",end=" ")
            case 2:
                print("TWO",end=" ")
            case 3:
                print("THREE",end=" ")
            case 4:
                print("FOUR",end=" ")
            case 5:
                print("FIVE",end=" ")
            case 6:
                print("SIX",end=" ")
            case 7:
                print("SEVEN",end=" ")
            case 8:
                print("EIGHT",end=" ")
            case 9:
                print("NINE",end=" ")
        r=r//10
    #IN THIS PROGRAM IF WE ENTER 3210 THEN THE O/T WILL BE
    # THREE TWO ONE .(ZERO) WILL NOT PRINT BECAUSE AS WE REVERSE THE DIGIT 0 CANT BE REVERSE