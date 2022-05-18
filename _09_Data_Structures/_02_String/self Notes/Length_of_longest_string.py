lst=['prahallad','pg','ramesh']

res = max(lst , key=len)
print(res)


#function
def long_length():
    lst=['rohit','pg','kartik','hardik']
    res = max(lst , key=len)
    return res
  
print(long_length())