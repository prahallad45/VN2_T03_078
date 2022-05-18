def find_even(n):
    for a in range(n):
        if a % 2 ==0:
            print(a)
find_even(10)        

# for a in range(20):
#     if a % 2 ==0:
#         print(a)
        
    
# harsha(x) = x^2 +1 


# f(2) = 5 
# f(3)  = 10
# name = 'harsha'
# print(name)
def my_func():
    return ( 'harsha')    
name = my_func()  
print(name + 'var')

def my_func2(just):
    return just    

name = 'ranjit'
out_name = my_func2(name)  
print(out_name + 'k')

names = ['harsha','ranjit','ram']

for each in names:
    print(my_func2(each))
    


def pass_list(lst1):
    out_lst = []
    for each in lst1:
        if each > 10:
            out_lst.append(each)
    return out_lst


greater = pass_list([10,3,15,23,1,15,9])
print(greater)



def multiple_param(b,a):
    print('value of a is :',a)
    print('value of b is :',b)
    return a + b

print(multiple_param(a = 10,b =20))




def multiple_param2(b=10,a = 5,c = 10):
    print('value of a is :',a)
    print('value of b is :',b)
    return a + b

print(multiple_param2())


a = multiple_param2
print(a)



def multiple(lst1: list):
    if lst1 is list:
        for each in lst1:
            print(each)
        return 'success'
    return 'fail'    
multiple([1])


def some_func():
    return 1,2,3

a,b,c = some_func()

print(a,b,c)
