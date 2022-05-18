print("\t<>"*10)
print("\t1 ADDICTION")
print("\t2 SUBTRACTION")
print("\t3 MULTIPLATION")
print("\t4 DIVISION")
print("\t5 MODULUS")
print("\t6 EXPONINCIAL")
print("\t7 EXIT")
print("\t<>"*10)
n=int(input("ENTER YOUR CHOICE:"))

match n:
    case 1:
        a=int(input("enter first number:"))
        b=int(input("enter second number:"))
        c=a+b
        print("sum of {} and {} is {} ".format(a,b,c))
    case 2:
        a=int(input("enter first number:"))
        b=int(input("enter second number:"))
        c=a-b
        print("sub of {} and {} is {} ".format(a,b,c))
    case 3:
        a=int(input("enter first number:"))
        b=int(input("enter second number:"))
        c=a*b
        print("mul of {} and {} is {} ".format(a,b,c))
    case 4:
        a=int(input("enter first number:"))
        b=int(input("enter second number:"))
        c=a%b
        print("div of {} and {} is {} ".format(a,b,c))
    case 5:
        a=int(input("enter first number:"))
        b=int(input("enter second number:"))
        c=a/b
        print("mod of {} and {} is {} ".format(a,b,c))
    case 6:
        a=int(input("enter first number:"))
        b=int(input("enter second number:"))
        c=a^b
        print("exp of {} and {} is {} ".format(a,b,c))
    case _:
        print("INVALID INPUT")
print("THANK YOU")
        