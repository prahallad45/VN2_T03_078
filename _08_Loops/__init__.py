str1 = 'harsha'
# 0
# for (i= 1 , i<5, i++)

for each in str1:
    print(each)
    
lst1 = [1.0,2,3,4,5,6]
for each in lst1:
    print(each)
    
for each in lst1:  # 1.0 2 3 4  5 6 
    if each % 2 ==0:
        print('even number',each)  
        if each > 4:
            print('im on the top')
    elif each > 3:
        print('im greater than 3')
    else:
        print('im the worst')
        
lst2 = ['harsha','ranjith']
for each in lst2:  # harsha
    for num in range(3):  # num = 0 ,1
        print('output',(each,num))  #harsha, 0 harsha,1
        




# output('harsha',0)
# output('harsha',1)
# output('harsha',2)
# output('ranjith',0)
# output('ranjith',1)
# output('ranjith',2)






# im the worst
# even number 2
# im the worst
# even number 4
# im greater than 3
# even number 6
# im on the top


# continue break pass List
i = 0 
while i < 5:  # 4 < 5 True
    print('harsha',i)  # harsha0
    if i == 4: # True
        print('im the greatest') 
        for each in range(3): # each = 2
            if each % 2 ==0:  # True
                print('super',(each,i))
            else:
                print('shutup')
    i += 1  # i =4
    
print('im below while')

# harsha 0
# harsha 1
# harsha 2
# harsha 3
# harsha 4
# im the greatest
# super(0,4)
# shutup 
# super(2,4)
# im below while