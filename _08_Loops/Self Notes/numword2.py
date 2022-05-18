n=input("ENTER A NUMBER:")
i=0
while (i<len(n)):
    d=n[i]
    match int(d):
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
    i=i+1
