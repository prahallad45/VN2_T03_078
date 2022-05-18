num =int(input("enter the number:"))

def fibinocci(n):
    pre_last, last = 0,1
    for each in range(n):
        yield pre_last
        pre_last, last = last, pre_last + last
        
print(list(fibinocci(num)))



# 2nd method

nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0

if nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1