x = 1
while x < 15:
    print(x)
    x += 1
    if x == 10:
        print('value of x is :', x) # print
        print('harahsa')
        print('after break')
        continue
    print('im not going to execute in continue')
print('im out of while ')

x = 3
y = 3
while x < 10: # x = 9
    while y < 5: # 4 <5 True
        print('first loop vaue :',y) #y = 3 4
        if y == 4:
            y += 1  # y = 4
            break # break
        y +=1
    print('secon loop value :',x)
    if x == 7:
        break
    x += 1


for a in range(10):
    print(a)
    pass

while True:
    pass

def name(**kwargs):
    pass
