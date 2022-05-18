def func(x):
    a=x[::-1]
    print(a)
func("prahallad")



class Student:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)
a=Student("pg")
a.show()