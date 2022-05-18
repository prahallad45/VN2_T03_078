a=int(input("Enter nos of student:"))
res={}
for i in range(a):
        sname = input("Enter names of student :")
        sper=input("Enter % of marks :")
        res[sname]=sper
print("name\tpercentage")   
for i,j in res.items():
    print(f'{i}\t{j}')

