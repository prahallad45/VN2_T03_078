#ACCEPT STUDENT NUMBER,NAME,3 MARKS AND CALCULATE TOTAL MARKS, % AND GRADE
while(True): #FOR VALIDATION
    sno=int(input("ENTER STUDENT NUMBER(1-100):"))
    if(sno>=0) and (sno<=100):
        break #TO GETOUT OF LOOP IF CONDITION IS SATISFIED
sname=input("ENTER STUUDENT NAME:")
while(True):
    c=int(input("ENTER MARK OF C:"))
    if(c>=0) and (c<=100):
        break
while(True):
    cpp=int(input("ENTER MARK OF C++:"))
    if(cpp>=0) and (cpp<=100):
        break
while(True):
    py=int(input("ENTER MARK OF PYTHON:"))
    if(py>=0) and (py<=100):
        break
tmark=c+cpp+py
percentage=(tmark/300)*100
if(c<40) or (cpp<40) or (py<40):
    grade="FAIL"
elif(tmark>=250) and (tmark<=300):
    grade="DISTINCTION"
elif(tmark>=200) and (tmark<=249):
    grade="FIRST"
elif(tmark>=150) and (tmark<=199):
    grade="SECOND"
else:
    grade="THIRD"
print("*"*40)
print("\tSTUDENT REPORT")
print("*"*40)
print("STUDENT NUMBER ={}".format(sno))
print("STUDENT NAME ={}".format(sname))
print("MARK IN C ={}".format(c))
print("MARK IN C++ ={}".format(cpp))
print("MARK IN PYTHON ={}".format(py))
print("TOTAL MARKS ={}".format(tmark))
print("PERCENTAGE ={}".format(percentage))
print("GRADE = {}".format(grade))
