d={"MONDAY":1,"TUESDAY":2,"WEDNESDAY":3,"THUSDAY":4,"FRIDAY":5,"SATURDAY":6,"SUNDAY":7}
w=input("ENTER WEEK NAME:")
if(d.get(w.upper())!=None):
    print(w)
else:
    match w.lower():
        case "mon"|"tue"|"wed"|"thus"|"fri":
            print("ITS WORKING DAY")
        case "sat":
            print("ITS SATURDAY")
        case "sun":
            print("HOLIDAY")
        case _:
            print("INVALID WEEK NAME")