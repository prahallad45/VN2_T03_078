#list all method
def allmethod(lst):
    print(f'original list={lst}')

    a=len(lst)
    print(f'length={a}')

    lst.append(10)
    print(f'append 10 {lst}')

    lst.insert(2,550)
    print(f'inserted 550 at 2nd index={lst}')

    lst1=lst.copy()
    print(f'copy lst to lst1 {lst}{lst1}')

    lst.remove(4)
    print(f'after remove of 4 {lst}')

    lst.pop()
    print(f'pop operation done {lst}')

    lst.extend(lst3)
    print(f'lst3 is extended to lst= {lst}\n {lst3}')

    l=lst.count(3)
    print(f'count of 3 in list:{l}')

lst1=[]
lst3=[20,40,60,80]
lst=[1,4,5,6,3,3,55,3,5,8,90]
allmethod(lst)