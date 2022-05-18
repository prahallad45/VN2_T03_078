x = "prahallad" #global

def myfunc():
  x = "gahir" #local 
  print(x,id(x))

myfunc()
print(x,id(x))

#-----------
def myfunc1():
    global x
    x=22
    print(x,id(x))
x=10
print(x,id(x))
myfunc1()
print(x,id(x))
#------------
print("-------------")

lst=[10,20,33]
print(lst,id(lst))
def myfunc2(pg):
    pg.append(44)
    print(lst,id(lst))

myfunc2(lst)
print(lst,id(lst))